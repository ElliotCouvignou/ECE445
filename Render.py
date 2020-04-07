import json
import os
import wave
import math
import numpy as np
import copy as copy
import DSP
import random
from pydub.utils import mediainfo
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from scipy import signal
from audio2numpy import open_audio
from scipy.io import wavfile


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        global result
        result = data.get('results')
        #print(result)


    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


# this is a class that holds all the parameters for each render feature in one class. This is so we dont
# flood the parameter space in each function header
class RenderSettings():
    def __init__(self):
        self.pauseShortenEnable = False;
        self.pauseShortenAmount = 0.0;
        self.pauseOverlap = []
        self.backgroundFillEnable = False;
        self.crossfadeEnable = False;
    
    def setPauseOverlap(self, new):
        self.pauseOverlap = new
        
class Transcript():
    def __init__(self):
        self.words = np.array(['wordwordwordwordwordword'])
        self.timestamps = np.array([0.00], dtype=object)
        self.shifts = np.array([0.00], dtype=object)

        self.enableBackgroundNoiseFill = False
    def initAudio(self, audio, sr):
        self.sr = sr
        
        try:        
            self.audio = audio
            if(len(audio.shape) == 1):
                print('Transcript Recognizes Mono audio')
                self.isMono = True
                self.isStereo = False
                self.audiolength = audio.shape[0]
                self.audio[0] += self.audio[1]  #test read-only
                
            elif(len(audio.shape) == 2):
                print('Transcript Recognizes Stereo audio')
                self.isMono = False
                self.isStereo = True
                self.audiolength = audio.shape[0]
                self.audio[0][0] += self.audio[0][1] #test read-only                
                            
        except:
            self.audio = copy.deepcopy(audio) # deepcopy our own array if read-only        
            #print(self.audio)
        self.lastRender = audio
        
    def copyother(self, transcript):
        self.words = copy.deepcopy(transcript.words)
        self.timestamps = copy.deepcopy(transcript.timestamps)
        
    def setupIBM(self, transcript, confidence):
        self.words = np.repeat(self.words, len(transcript))
        self.timestamps = np.repeat(self.timestamps, len(transcript))
        self.confidence = confidence
        
        i = 0
        for word in transcript:
            self.words[i] = word[0]
            self.timestamps[i] = (word[1],word[2])
            i += 1
        
        self.wordCount = len(self.timestamps)
        self.shifts = np.zeros(self.wordCount)

    def swap(self, i, j):
        tmp = self.words[j]
        self.words[j] = self.words[i]
        self.words[i] = tmp

        tmp = self.timestamps[j]
        self.timestamps[j] = self.timestamps[i]
        self.timestamps[i] = tmp

        tmp = self.shifts[j]
        self.shifts[j] = self.shifts[i]
        self.shifts[i] = tmp

    def getSpec(self):
        if(self.isMono):
            f, t, spec = signal.spectrogram(self.audio, self.sr)
        else:
            f, t, specl = signal.spectrogram(self.audio[:,0], self.sr)
            f, t, specr = signal.spectrogram(self.audio[:,1], self.sr)
            spec = (specl + specr) / 2
        #spec = DSP.stft(input_sound=self.audio, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
        #t,f = DSP.FormatAxis(spec, self.sr, len(self.audio)/self.sr)
        return spec, t, f


    # Gathers around 8 secs of background noise if possible, want to play it back at random initial phases 
    def sampleBackgroundNoise(self):
        # Can only be done if we know pauses
        if(len(self.pauses) == 0):
            print('nopauses')
            return
    
        # this is going to be 8 sec sample of background noise 
        maxBGNlength = round(8*self.sr)
        if(self.isStereo):
            self.backgroundNoise = np.zeros(2*maxBGNlength).reshape(maxBGNlength, 2)
        else:
            self.backgroundNoise = np.zeros(maxBGNlength)

        # sample background with pauses
        curidx = 0      
        for i in range(len(self.pauses)):
            pause = (int(self.pauses[i][0]*self.sr), int(self.pauses[i][1]*self.sr))
            sliced = self.audio[pause[0]:pause[1]]
            l = len(sliced)

            if(curidx+l >= maxBGNlength):
                l = maxBGNlength - curidx - 1
            self.backgroundNoise[curidx:curidx+l] = sliced[:l]
            curidx = curidx+l
            
            if(curidx+l >= maxBGNlength):
                break

        self.enableBackgroundNoiseFill = True
        print('Finish Sampling')


    # creates main channel type transcript from others. Basically combines them
    def MainFromOthers(self, transcripts):
        
        for i in range(len(transcripts)):
            transcript = transcripts[i]
            if( i == 0):
                self.words = transcript.words
                self.timestamps = transcript.timestamps
            else:
                self.words = np.hstack((self.words, transcript.words))
                self.timestamps = np.hstack((self.timestamps, transcript.timestamps))
        
        self.audiolength = len(self.timestamps)
        self.shifts = [(0.0, 0.0)] * self.audiolength
        self.quicksort( ( 0, self.audiolength-1) )    
        

    # trans = transcript array to find overlapping pauses 
    def findPauses(self):
        # format of self.pauses is tuple ranges of pauses (like timestamps)
        self.pauses = []
        curtime = 0.0
        # this is prettty much taking the inverse of timestamps
        for i in range(len(self.timestamps)):
            times = self.timestamps[i]            
            tup = (0.0, 0.0)
            if(times[0] > curtime):
                tup = (curtime, times[0])
                self.pauses.append(tup)

            # set maerker to end of spoken word     
            curtime = times[1] 

        # check from here until end of audio
        if(curtime < len(self.audio) / self.sr):
            tup = (curtime, len(self.audio) / self.sr)
            self.pauses.append(tup)
        
        self.pauses = np.asarray(self.pauses)

    # trans = transcript array of transcripts with their self.pauses already filled
    def findOverlappingPauses(self, trans, RenderSettings):
        numchannels = len(trans)
        # same format as timestamps
        pauseOverlap = []
        channel_iters = [0] * numchannels
        #dt = np.dtype(trans[0].pauses)
        Rtime = 0.0
        Ltime = 0.0
        done = False
        # method: find intervals, go trhough channel 0's pauses and see any overlaps from there
        for i in range(len(trans[0].pauses)):
            currentPause = trans[0].pauses[i]

            Ltime = currentPause[0]
            Rtime = currentPause[1]
            # through each channel from 1 onwards
            thisIntersection = currentPause
            inInterval = False
            for c in range(1,numchannels):
                # through last seen puase on channel until end
                for p in range(channel_iters[c], len(trans[c].pauses)):
                    # find and intersect with currentPause
                    thisPause = trans[c].pauses[p]
                    
                    intersection = self.getIntersection(thisPause, thisIntersection)
                    if(intersection != None):
                        # check down other channels
                        thisIntersection = intersection
                        inInterval = True
                    
                    # check if thisPause[0] within current range
                    #inRange = False
                    #if(Ltime <= thisPause[0] and Rtime >= thisPause[0]):
                    #    Ltime = thisPause[0]
                    #    inRange = True
                    #    channel_iters[c] = p
                    #if(Ltime <= thisPause[1] and Rtime >= thisPause[1]):
                    #    Rtime = thisPause[1]
                    #    inRange = True
                    #    channel_iters[c] = p
                    #
                    #if(inRange):
                    #    # force break out  p loop onto next c
                    #    p = len(trans[c].pauses) - 1
                    #elif(p == len(trans[c].pauses)-1):
                    #    # if we reached end of this, then no interval so skip rest of channels
                    #    inInterval = False
                    #    c = len(trans[c].pauses)
            if(inInterval):
                pauseOverlap.append(thisIntersection)       
        
        print(pauseOverlap)

    # helper function for above
    def getIntersection(self, interval_1, interval_2):
        start = max(interval_1[0], interval_2[0])
        end = min(interval_1[1], interval_2[1])
        if start < end:
            return (start, end)
        return None
        
    #
    # Transcript.words[i] = i-th word
    # Transcript.timestamps[i] = start/end times for i-th word
    #
    def RenderTranscription(self, trans, RenderSettings):
        render = np.asarray(trans.audio, dtype=np.float)
        render = render.transpose()
        renderlen = trans.audiolength
        time = trans.timestamps
        print('dorender')
        
        # ATM doinglinear crossfade (75ms) via np.linspace
        delay_ms = round(.075 * trans.sr) # 75 ms for now. based on feel, FOR WINDOWING

        # loop through each word, if shifts[i] !=0 then edit audio array to shift word slice
        for i in range(len(trans.words)):
            
            if(trans.shifts[i] != 0.0 ):
                # get start/end times in samples for slicing
                newstart_n = time2sample(time[i][0],trans.sr)
                newend_n = time2sample(time[i][1],  trans.sr)  
                oldstart_n = time2sample(time[i][0] - trans.shifts[i],trans.sr) # undo shift applied to timestamps
                oldend_n = time2sample(time[i][1] - trans.shifts[i],trans.sr)  # undo shift applied to timestamps

                shift = trans.shifts[i]
                sliced = trans.audio[oldstart_n:oldend_n]
                if(trans.isStereo):
                    sliced = sliced.transpose()

                # extend/pad render length if necessary
                if(newend_n > renderlen):  
                    l = newend_n - renderlen

                    #mono/stereo pad cases
                    if(trans.isStereo):
                        pad = np.zeros(l*2).reshape(2,l)
                    else:
                        pad = np.zeros(l)
                    if(renderlen == 0):
                        render = pad
                    else:
                        # if windowing, window end piece
                        if(RenderSettings.crossfadeEnable and renderlen == trans.audiolength):
                            if(trans.isStereo):
                                render[:,-delay_ms:] *= np.linspace(1.0, 0.0, min(delay_ms, renderlen))
                            else:
                                render[-delay_ms:] *= np.linspace(1.0, 0.0, min(delay_ms, renderlen))
                        render = np.hstack((render, pad))

                    renderlen = newend_n
                # check if new timestamp is before 0seconds
                elif(newstart_n < 0):
                    offset = abs(newstart_n)
                    pad = np.zeros(offset)
                    render = np.hstack((pad, render))
                    # shift new/old start/end times since newstart_n should index 0 now
                    newend_n += offset
                    newstart_n += offset
                    oldend_n += offset
                    oldstart_n += offset

                # place audio slice into render
                # if we are windowing then we need to crossfade before slice, after slice, and both sides of slice
                if(RenderSettings.crossfadeEnable):
                    # windowing slcied audio first
                    # this is complicated, if trans.shifts[i+1] == shifts[i] then these words are in the same segment
                    # if this is true we dont window their connections since they are still one piece
                    if(i > 0): #boundary control
                        #  check if left word is connected to right
                        leftwordend_n = time2sample(trans.timestamps[i-1][1], trans.sr)
                        
                        if(leftwordend_n != newstart_n):
                            # left index word isn't connected
                            # window left side of this audio and right side of audio before this word                            
                            #mono/stereo
                            if(trans.isStereo):
                                #print(sliced.shape)
                                sliced[0, :delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[0,:delay_ms]).astype(int)
                                sliced[1, :delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[1,:delay_ms]).astype(int)
                                render[0, oldstart_n-delay_ms:oldstart_n] *= np.linspace(1.0, 0.0, delay_ms)
                                render[1, oldstart_n-delay_ms:oldstart_n] *= np.linspace(1.0, 0.0, delay_ms)
                            else:
                                sliced[:delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, len(sliced)))*sliced[:delay_ms]).astype(int)
                                render[oldstart_n-delay_ms:oldstart_n] *= np.linspace(1.0, 0.0, delay_ms)
                    else:
                        #unique case, if i = 0 and shift != 0, window left no matter what
                        #mono/stereo
                        if(trans.isStereo):
                            #print(sliced.shape)
                            sliced[0, :delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[0,:delay_ms]).astype(int)
                            sliced[1, :delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[1,:delay_ms]).astype(int)
                        else:
                            sliced[:delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, len(sliced)))*sliced[:delay_ms]).astype(int)

                    if(i < trans.wordCount-1):
                        rightwordstart_n = time2sample(trans.timestamps[i+1][0], trans.sr)
                        
                        if(rightwordstart_n != newend_n):
                            # right word isnt in same segment, window
                            #print('right', i, rightwordstart_n, newend_n)
                            #mono/stereo
                            if(trans.isStereo):
                                #print(sliced.shape)
                                sliced[0,:delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[0,:delay_ms]).astype(int)
                                sliced[1,:delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, sliced.shape[1]))*sliced[1,:delay_ms]).astype(int)
                                render[0, oldend_n:oldend_n+delay_ms] *= np.linspace(0.0, 1.0, delay_ms)
                                render[1, oldend_n:oldend_n+delay_ms] *= np.linspace(0.0, 1.0, delay_ms)
                            else:
                                sliced[:delay_ms] = (np.linspace(0.0,1.0 ,min(delay_ms, len(sliced)))*sliced[:delay_ms]).astype(int)
                                render[oldend_n:oldend_n+delay_ms] *= np.linspace(0.0, 1.0, delay_ms)
                
                # move sliced audio and zero pad empty space
                if(trans.isStereo):
                    render[:, newstart_n:newend_n] += sliced
                    
                    if(self.enableBackgroundNoiseFill and RenderSettings.enableBackgroundNoiseFill):
                        print('?')
                        self.renderBackgroundNoiseFill(render[:, oldstart_n:oldend_n])                        
                    else:                        
                        render[:, oldstart_n:oldend_n] = 0

                else:
                    render[newstart_n:newend_n] += sliced

                    if(self.enableBackgroundNoiseFill and RenderSettings.enableBackgroundNoiseFill):
                        print('?')
                        self.renderBackgroundNoiseFill(render[:, oldstart_n:oldend_n])                        
                    else:                        
                        render[:, oldstart_n:oldend_n] = 0
                # !!!!!!!!!BACKGROUND FILL GOES HERE!!!!!!!!!!
        
        self.lastRender = render.T
        return render

    def renderBackgroundNoiseFill(self, renderslice):
        length = len(renderslice)
        maxBGNlength = round(8*self.sr)
        delay_ms = round(.075 * trans.sr) # 75 ms for now. based on feel, FOR WINDOWING

        curlength = 0
        print('Filling BGN')
        while(curlength < length):
            # sample 3.5 seconds of sampled background, repeat on different starting points
            lennoise = min(length - curlength, round(3.5*self.sr))
            start = random.randint(0, maxBGNlength-1)
            end = (start + lennoise) % maxBGNlength
            if(end < start):
                noise = self.backgroundNoise[start:] + self.backgroundNoise[:end]
            else:
                noise = self.backgroundNoise[start:end]
            # window both ends of noise 
            noise[:delay_ms] *= np.linspace(0.0, 1.0, delay_ms)
            noise[-delay_ms:] *= np.linspace(1.0, 0.0, delay_ms)

            if(curlength != 0):
                curlength -= delay_ms
            renderslice[curlength:curlength+lennoise] = noise

            curlength += lennoise
        print('done Filling BGN')

        
    def setAudioAsRender(self):
        self.audio = self.lastRender

    # calls Render Transcription for each channel
    # parameters are arrays where each index are parameters to individual render transcription calls
    def RenderMultiChannels(self, oldtrans, newtrans, audios, srs, window=False):
        render = np.array([0])
        for i in len(oldtrans):
            render += self.RenderTranscription(oldtrans[i], newtrans[i], audios[i], srs[i], window)
        return render

    
    # next two are for sorting transcription words based on timestamps
    def partition(self, low, high):
        # We select the middle element to be the pivot. Some implementations select
        # the first element or the last element. Sometimes the median value becomes
        # the pivot, or a random one. There are many more strategies that can be
        # chosen or created.
        pivot = self.timestamps[(low + high) // 2][0]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while self.timestamps[i][0] < pivot:
                i += 1

            j -= 1
            while self.timestamps[j][0] > pivot:
                j -= 1

            if i >= j:
                return j

            # At this poimt i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot)
            self.swap(i, j)

    def _quick_sort(self, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            
            split_index = self.partition(low, high)
            self._quick_sort(low, split_index)
            self._quick_sort(split_index + 1, high)

    def quicksort(self, range):
        # Create a helper function that will be called recursively
        self._quick_sort(range[0], range[1])
   
    def ibm_recog(self,audioname,audiofp):
        authenticator = IAMAuthenticator('6noBhxJHkbRVsgbxsl47v6dFZnJdoRRrDRYte7GgKKxu')
        speech_to_text = SpeechToTextV1(authenticator=authenticator)
        speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/51085e72-7959-4c18-94cd-d4d874baf61d')
        myRecognizeCallback = MyRecognizeCallback()
        ts = []
        c = []
    
        with open(join(dirname(audioname), audiofp), 'rb') as audio_file:
        
            audio_source = AudioSource(audio_file)
        
            x = speech_to_text.recognize_using_websocket(
                audio=audio_source,
                content_type='audio/mp3',
                inactivity_timeout = -1,
                recognize_callback=myRecognizeCallback,
                model='en-US_BroadbandModel',
                timestamps=True,
                smart_formatting=True,
            )
            
        for r in result:
            alternatives = r.get('alternatives')
            ts.append(alternatives[0].get('timestamps'))
            timestamps = [elem for twod in ts for elem in twod] 
            c.append(alternatives[0].get('confidence'))
            confidence = sum(c)/len(c)  
        a,sr=open_audio(audiofp)
        self.initAudio(a,sr)
        self.setupIBM(timestamps,confidence)



def time2sample(time, sr):
    return int(round(time*sr))

#--------------------------------------------------------------------------------







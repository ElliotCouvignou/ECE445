import json
import os
import wave
import math
import numpy as np
import copy as copy
import DSP
from pydub.utils import mediainfo
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from scipy import signal
from audio2numpy import open_audio

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))
        
class Transcript():
    def __init__(self):
        self.words = np.array(['wordwordwordwordwordword'])
        self.timestamps = np.array([0.00], dtype=object)


    def initAudio(self, audio, sr):
        self.audio = audio
        self.sr = sr
        
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

    def swap(self, i, j):
        tmp = self.words[j]
        self.words[j] = self.words[i]
        self.words[i] = tmp

        tmp = self.timestamps[j]
        self.timestamps[j] = self.timestamps[i]
        self.timestamps[i] = tmp

    def getSpec(self):
        spec = DSP.stft(input_sound=self.audio, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
        t,f = DSP.FormatAxis(spec, self.sr, len(self.audio)/self.sr)
        return spec, t, f

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

        self.quicksort()        
        
    #
    # Transcript.words[i] = i-th word
    # Transcript.timestamps[i] = start/end times for i-th word
    #
    def RenderTranscription(self, oldtrans, newtrans, windowing=False):
        render = np.array([0])
        renderlen = 0

        newtime = newtrans.timestamps
        oldtime = oldtrans.timestamps
        # loop through each word, if this is latest word then extend render
        idx = 0
        for i in range(len(oldtrans.words)):

            # get start/end times in samples for slicing
            oldstart_n = time2sample(oldtime[i][0],oldtrans.sr)
            oldend_n = time2sample(oldtime[i][1],  oldtrans.sr)
            newstart_n = time2sample(newtime[i][0],oldtrans.sr)
            newend_n = time2sample(newtime[i][1],  oldtrans.sr)    

            shift = newstart_n - oldstart_n

            if(newend_n > renderlen):  
                # extend render length 
                l = newend_n - renderlen
                pad = np.zeros(l)
                if(renderlen == 0):
                    render = pad
                else:
                    render = np.hstack((render, pad))
                renderlen = len(render)

            # place audio slice into render
            if(windowing and shift != 0):
                # ATM trying out Hamming for minimal spectral coloring
                windowed = np.asarray(oldtrans.audio[oldstart_n:oldend_n], dtype=np.float)

                delay_ms = round(.075 * oldtrans.sr) # 75 ms for now. based on feel
                windowed[:delay_ms] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # front
                windowed[-delay_ms:] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # end

                render[newstart_n:newend_n] += windowed
            else:
                render[newstart_n:newend_n] += oldtrans.audio[oldstart_n:oldend_n]
            idx += 1

        newtrans.audio = render
        newtrans.sr = oldtrans.sr
        return render


    # calls Render Transcription for each channel
    # parameters are arrays where each index are parameters to individual render transcription calls
    def RenderMultiChannels(self, oldtrans, newtrans, audios, srs, window=False):
        for i in len(oldtrans):
            self.RenderTranscription(oldtrans[i], newtrans[i], audios[i], srs[i], window)


    
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

    def quicksort(self):
        # Create a helper function that will be called recursively
        self._quick_sort(0, len(self.timestamps) - 1)
   
    def ibm_recog(self,audioname,audiofp,ctype):
        authenticator = IAMAuthenticator('6noBhxJHkbRVsgbxsl47v6dFZnJdoRRrDRYte7GgKKxu')
        speech_to_text = SpeechToTextV1(authenticator=authenticator)
        speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/51085e72-7959-4c18-94cd-d4d874baf61d')
        myRecognizeCallback = MyRecognizeCallback()
    
        with open(join(dirname(audioname), audiofp), 'rb') as audio_file:
        
            audio_source = AudioSource(audio_file)
        
            x = speech_to_text.recognize(
                audio=audio_file,
                content_type=ctype,
                recognize_callback=myRecognizeCallback,
                model='en-US_BroadbandModel',
                timestamps=True,
            #smart_formatting=True
            )
        result = x.result
        alternatives = result.get('results')[0].get('alternatives')[0]
        transcript = alternatives.get('transcript')
        timestamps = alternatives.get('timestamps')
        confidence = alternatives.get('confidence')
        a,sr=open_audio(audiofp)
        self.initAudio(a,sr)
        self.setupIBM(timestamps,confidence)



def time2sample(time, sr):
    return round(time*sr)

#--------------------------------------------------------------------------------








from scipy import signal

# stuff
import math
import numpy as np
import copy as copy




### CLASSES ####


# Transcript datatype-ish class
class Transcript():
    def __init__(self):
        self.words = np.array(['wordwordwordwordwordword'])
        self.timestamps = np.array([0.0], dtype=object)


    def initAudio(self, audio, sr):
        self.audio = audio
        self.sr = sr
        
    def copyother(self, transcript):
        self.words = copy.deepcopy(transcript.words)
        self.timestamps = copy.deepcopy(transcript.timestamps)
        
    def setupGoogle(self, transcript):
        self.words = np.repeat(self.words, len(transcript))
        self.timestamps = np.repeat(self.timestamps, len(transcript))
        
        i = 0
        for word in transcript:
            self.words[i] = word.word
            self.timestamps[i] = (word.start_time.seconds + word.start_time.nanos / 10**9 , \
                                  word.end_time.seconds + word.end_time.nanos / 10 ** 9)
            i += 1

    def swap(self, i, j):
        self.words[i], self.words[j] = self.words[j], self.words[i]
        self.timestamps[i], self.timestamps[j] = self.timestamps[j], self.timestamps[i]
        

    #
    # Transcript.words[i] = i-th word
    # Transcript.timestamps[i] = start/end times for i-th word
    #
    def RenderTranscription(self, oldtrans, newtrans, audio, sr, windowing=False):
        render = np.array([0])
        renderlen = 0

        newtime = newtrans.timestamps
        oldtime = oldtrans.timestamps
        # loop through each word, if this is latest word then extend render
        idx = 0
        for i in range(len(oldtrans.words)):

            # get start/end times in samples for slicing
            oldstart_n = time2sample(oldtime[i][0],sr)
            oldend_n = time2sample(oldtime[i][1],sr)
            newstart_n = time2sample(newtime[i][0],sr)
            newend_n = time2sample(newtime[i][1], sr)    

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
                windowed = np.asarray(audio[oldstart_n:oldend_n], dtype=np.float)

                delay_ms = round(.075 * sr) # 75 ms for now. based on feel
                windowed[:delay_ms] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # front
                windowed[-delay_ms:] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # end

                render[newstart_n:newend_n] += windowed
            else:
                render[newstart_n:newend_n] += audio[oldstart_n:oldend_n]
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
        print(self.words)
        print(self.timestamps)






def time2sample(time, sr):
    return round(time*sr)
        
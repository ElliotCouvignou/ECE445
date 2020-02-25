
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




#
# Transcript.words[i] = i-th word
# Transcript.timestamps[i] = start/end times for i-th word
#
def RenderTranscription(oldtrans, newtrans, audio, sr, windowing=False):
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
            renderlen += l
            
        # place audio slice into render
        if(windowing and shift != 0):
            # ATM trying out Hamming for minimal spectral coloring
            windowed = np.asarray(audio[oldstart_n:oldend_n], dtype=np.float)
            
            delay_ms = round(.075 * sr) # 75 ms for now. based on feel
            windowed[:delay_ms] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # front
            windowed[-delay_ms:] *= np.linspace(0.0,1.0 ,min(delay_ms, len(windowed)))  # end
            
            render[newstart_n:newend_n] = windowed
        else:
            render[newstart_n:newend_n] = audio[oldstart_n:oldend_n]
        idx += 1
    
    return render


# calls Render Transcription for each channel
# parameters are arrays where each index are parameters to individual render transcription calls
def RenderMultiChannels(oldtrans, newtrans, audios, srs, window=False):
    for i in len(oldtrans):
        RenderTranscription(oldtrans[i], newtrans[i], audios[i], srs[i], window)
        
        
# interface function from ui app
def RenderCall(oltranscript, newtranscript):
    
    print(newtranscript.words)
    print(newtranscript.timestamps)

def time2sample(time, sr):
    return round(time*sr)
        
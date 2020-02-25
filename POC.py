### REAL POC CELL ##

"""
Created on Mon Feb 10 16:36:55 2020
No stealy 
@author: ecouv
"""
# Qt5 related stuff
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon

from PyQt5 import QtWidgets

import sys
sys.path.insert(0, 'UserInterface/')
from GUI import Ui_TranscriptEditor


# transcription library stuff
from google.cloud import speech_v1
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg') # for QT5

# stuff
import math
import numpy as np
import time
import speech_recognition as sr
import os

import copy




### CLASSES ####


# Transcript datatype-ish class
class Transcript():
    def __init__(self):
        self.words = np.array(['wordwordwordwordwordword'])
        self.timestamps = np.array([0.0], dtype=object)
        
    def setupGoogle(self, transcript):
        self.words = np.repeat(self.words, len(transcript))
        self.timestamps = np.repeat(self.timestamps, len(transcript))
        
        i = 0
        for word in transcript:
            self.words[i] = word.word
            self.timestamps[i] = (word.start_time.seconds + word.start_time.nanos / 10**9 , \
                                  word.end_time.seconds + word.end_time.nanos / 10 ** 9)
            i += 1

    
def sample_long_running_recognize(storage_uri):
    """
    Print start and end time of each word spoken in audio file from Cloud Storage

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.flac'

    # When enabled, the first result returned by the API will include a list
    # of words and the start and end time offsets (timestamps) for those words.
    enable_word_time_offsets = True

    # The language of the supplied audio
    language_code = "en-US"
    config = {
        "enable_word_time_offsets": enable_word_time_offsets,
        "language_code": language_code,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for transcription to complete...")
    response = operation.result()

    # The first result includes start and end time word offsets
    result = response.results[0]
    # First alternative is the most probable result
    alternative = result.alternatives[0]
    print(u"Transcription complete...")
 
        
    return alternative.words

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
        

# shifts by unit of time in seconds
def ShiftTranscriptWord(transcript, index, timeshift):
    
    secs = int(timeshift)
    nanos = int((timeshift - secs) * 10**9)
    
    word = transcript[index]
    
    if(word.start_time.nanos + nanos >= 10**9):
        secs += 1
    if(word.end_time.nanos + nanos >= 10**9):
        secs += 1
    
    word.start_time.seconds += secs
    word.end_time.seconds += secs

    word.start_time.nanos = (word.start_time.nanos + nanos ) % 10**9
    word.end_time.nanos = (word.end_time.nanos + nanos ) % 10**9




    
    
#### START ####
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="JSON/My First Project-1534988de9b5.json"

storage_uri = 'gs://ringr_audio/venv/RawAudio/case1.wav'
    
    
sr, case2 = wavfile.read('RawAudio/case1.wav')  
transcript = sample_long_running_recognize(storage_uri)


# create deepcopy to prevent reference copying
newtrans = copy.deepcopy(np.asarray(transcript))


# MAKE NEW TRANSCRIPT

# shift 'top' word by 3 seconds
# case2 only has 7 detected words
# PARAMETERS: TRANSCRIPT, WORDINDEX, TIMESHIFT(+/-seconds)
ShiftTranscriptWord(newtrans, 0, 0)
ShiftTranscriptWord(newtrans, 1, 0)
ShiftTranscriptWord(newtrans, 2, 0)
ShiftTranscriptWord(newtrans, 3, 0)
ShiftTranscriptWord(newtrans, 4, 0)
ShiftTranscriptWord(newtrans, 5, 0)
ShiftTranscriptWord(newtrans, 6, 0)


# translate API transcript to one easier to use
gtranscript = Transcript()
gtranscript.setupGoogle(transcript)
gnewtrans = Transcript()
gnewtrans.setupGoogle(newtrans)


# get new audio from new transcript
newsound = RenderTranscription(gtranscript, gnewtrans, case2, sr, windowing=True)
newsoundf = RenderTranscription(gtranscript, gnewtrans, case2, sr, windowing=False)


## plot spectrograms with audio widget
sound(case2, sr, 'old sound')

# GUI TESTING
print('Launching UI')
qApp = QtWidgets.QApplication(sys.argv)

# aw = ApplicationWindow, currently using TranscriptEditor from qtdesign
aw = Ui_TranscriptEditor()
aw.setupUi(aw)

 
# plot spectrogram
spec = stft(input_sound=case2, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
t,f = FormatAxis(spec, sr, len(case2)/sr)
aw.plotOldSpec(spec, t, f)


# print transcription
aw.initTranscriptEditor(gtranscript)
aw.setTranscriptText(gtranscript)


aw.show()
sys.exit(qApp.exec_())

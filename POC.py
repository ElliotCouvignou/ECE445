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
from Render import Transcript


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

# translate API transcript to one easier to use
gtranscript = Transcript()
gtranscript.setupGoogle(transcript)
gtranscript.initAudio(case2, sr)


# audio widget
sound(case2, sr, 'old sound')

# GUI TESTING
print('Launching UI')
qApp = QtWidgets.QApplication(sys.argv)

# aw = ApplicationWindow, currently using TranscriptEditor from qtdesign
aw = Ui_TranscriptEditor()
aw.setupUi(aw)
aw.setupUiManual()

 
# plot spectrogram
spec = stft(input_sound=case2, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
t,f = FormatAxis(spec, sr, len(case2)/sr)
aw.plotOldSpec(spec, t, f)

# print transcription
aw.initTranscriptEditor(gtranscript)
aw.setTranscriptText(gtranscript)


aw.show()
sys.exit(qApp.exec_())

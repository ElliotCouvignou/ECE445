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


   
    
#### START ####

a = 'asd' #input('hardcode input (default)? or manual(m)? ')

if(a == 'm'):
    a = input('enter Google storage location e.g: gs://ringr_audio/venv/RawAudio/case1.wav : ')
    storage_uri = a
    a = input('enter local file location e.g: RawAudio/case1.wav : ')
    sr, case2 = wavfile.read(a)
    
else:
    # ONLY CHANGE THESE VARLAIBELS
    storage_uri1 = 'gs://ringr_audio/venv/RawAudio/case1.wav' 
    storage_uri2 = 'gs://ringr_audio/venv/RawAudio/case2.wav' 
    # google cloud API
    #storage_uri = 'gs://ringr_audio/venv/wetransfer-9e/case1.wav' 
    sr1, case1 = wavfile.read('RawAudio/case1.wav')                                           # local read
    sr2, case2 = wavfile.read('RawAudio/case2.wav')   
    

# no user inputon this    
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="JSON/My First Project-1534988de9b5.json"   # JSON API KEY
# do transcription    
gtranscript1 = sample_long_running_recognize(storage_uri1)
gtranscript2 =  sample_long_running_recognize(storage_uri2)

# translate API transcript to one easier to use
transcript1 = Transcript()
transcript1.setupGoogle(gtranscript1)
transcript1.initAudio(case1, sr1)

transcript2 = Transcript()
transcript2.setupGoogle(gtranscript2)
transcript2.initAudio(case2, sr2)

# GUI TESTING
print('Launching UI')
qApp = QtWidgets.QApplication(sys.argv)

# aw = ApplicationWindow, currently using TranscriptEditor from qtdesign
aw = Ui_TranscriptEditor()
aw.setupUi(aw)
aw.setupUiManual()

tarray = [transcript1, transcript2]
aw.launchInit(tarray, 2)

aw.show()
sys.exit(qApp.exec_())

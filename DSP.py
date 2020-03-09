### THIS FILE IS JUST FOR 3RD PARTY FUNCTIONS ### 
# transcription library stuff
from scipy.io import wavfile
from scipy import signal

# stuff
import math
import numpy as np
import time

import copy

def sound( x, rate=8000, label=''):
    from IPython.display import display, Audio, HTML
    if label is '':
        display( Audio( x, rate=rate))
    else:
        display( HTML( 
        '<style> table, th, td {border: 0px; }</style> <table><tr><td>' + label + 
        '</td><td>' + Audio( x, rate=rate)._repr_html_()[3:] + '</td></tr></table>'
        ))


def stft( input_sound, dft_size, hop_size, zero_pad, window=1.0):
    length = len(input_sound)
    
    # Part1. splitting into frames
    FrameAmount = math.ceil((length) / hop_size) + 1
    slices = np.arange(dft_size * FrameAmount).reshape(dft_size, FrameAmount)
    # set slices into array
    for i in range(FrameAmount):
        start = i * hop_size
        end = start + dft_size
        
        data = input_sound[start:end]
        
        # input too short... need to zero padd end
        if(data.shape[0] < dft_size):
            zero_padd = np.zeros(dft_size - data.shape[0])
            data = np.hstack((data, zero_padd))
           
        slices[:,i] = data * window
        
    #  Part2. Do fft of input slices        
    size = dft_size+zero_pad   
    if(size%2 ==0):
        NumBins = ((size) // 2) + 1
    else:
        NumBins = ((size) + 1) // 2
    
    NumBins = int(NumBins)
    f = np.arange(NumBins * FrameAmount, dtype=np.complex_).reshape(NumBins, FrameAmount)   
    f[:,:] = 0. + 0.j
    
    for i in range(FrameAmount):
        f[:,i] = np.fft.rfft(slices[:,i], size)      

    # Return a complex-valued spectrogram (frequencies x time)
    return f

def FormatAxis(specArray, sr, time):
    length = specArray.shape[1]
    numbins = specArray.shape[0]
    timeline = np.linspace(0, time, length)
    freqline = np.linspace(0, sr/2, numbins)
    #freqline = np.fft.fftfreq(numbins, d=1./sr)
    return timeline, freqline

def time2sample(time, sr):
    return round(time*sr)

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v/norm


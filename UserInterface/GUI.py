# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
# Uncomment this line before running, it breaks sphinx-gallery builds
# from PyQt5 import QtCore, QtWidgets

import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from scipy import signal
import math

from TranscriptPlotTab import TranscriptPlotFrame   
from TranscriptEditorTab import TranscriptEditorFrame
from Render import Transcript
from DSP import stft, FormatAxis, sound


class Ui_TranscriptEditor(QMainWindow):
    def setupUi(self, TranscriptEditor):
        TranscriptEditor.setObjectName("TranscriptEditor")
        TranscriptEditor.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TranscriptEditor.sizePolicy().hasHeightForWidth())
        TranscriptEditor.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(TranscriptEditor)
        self.gridLayout.setObjectName("gridLayout")
        self.TabWidget = QtWidgets.QTabWidget(TranscriptEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        self.TabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TabWidget.setAutoFillBackground(True)
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OriginalChannelTabs = QtWidgets.QTabWidget(self.tab1)
        self.OriginalChannelTabs.setObjectName("OriginalChannelTabs")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.OldTransFrame = QtWidgets.QFrame(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldTransFrame.sizePolicy().hasHeightForWidth())
        self.OldTransFrame.setSizePolicy(sizePolicy)
        self.OldTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OldTransFrame.setAutoFillBackground(True)
        self.OldTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.OldTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OldTransFrame.setObjectName("OldTransFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.OldTransFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.oldwords = QtWidgets.QTextEdit(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldwords.sizePolicy().hasHeightForWidth())
        self.oldwords.setSizePolicy(sizePolicy)
        self.oldwords.setObjectName("oldwords")
        self.gridLayout_3.addWidget(self.oldwords, 0, 0, 1, 2)
        self.OldSpecScrollBar = QtWidgets.QScrollBar(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldSpecScrollBar.sizePolicy().hasHeightForWidth())
        self.OldSpecScrollBar.setSizePolicy(sizePolicy)
        self.OldSpecScrollBar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.OldSpecScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.OldSpecScrollBar.setObjectName("OldSpecScrollBar")
        self.gridLayout_3.addWidget(self.OldSpecScrollBar, 2, 0, 1, 2)
        self.oldspec_plot = QtWidgets.QWidget(self.OldTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldspec_plot.sizePolicy().hasHeightForWidth())
        self.oldspec_plot.setSizePolicy(sizePolicy)
        self.oldspec_plot.setObjectName("oldspec_plot")
        self.gridLayout_3.addWidget(self.oldspec_plot, 1, 0, 1, 2)
        self.gridLayout_8.addWidget(self.OldTransFrame, 0, 0, 1, 1)
        self.OriginalChannelTabs.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.OriginalChannelTabs, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RenderButton = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderButton.sizePolicy().hasHeightForWidth())
        self.RenderButton.setSizePolicy(sizePolicy)
        self.RenderButton.setIconSize(QtCore.QSize(18, 18))
        self.RenderButton.setObjectName("RenderButton")
        self.gridLayout_6.addWidget(self.RenderButton, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6.addWidget(self.frame, 2, 0, 1, 1)
        self.EditorChannelsTab = QtWidgets.QTabWidget(self.tab)
        self.EditorChannelsTab.setObjectName("EditorChannelsTab")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.EditTransFrame = QtWidgets.QFrame(self.tab_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditTransFrame.sizePolicy().hasHeightForWidth())
        self.EditTransFrame.setSizePolicy(sizePolicy)
        self.EditTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EditTransFrame.setAutoFillBackground(True)
        self.EditTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.EditTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EditTransFrame.setObjectName("EditTransFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.EditTransFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.newwords_2 = QtWidgets.QTextEdit(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newwords_2.sizePolicy().hasHeightForWidth())
        self.newwords_2.setSizePolicy(sizePolicy)
        self.newwords_2.setObjectName("newwords_2")
        self.gridLayout_7.addWidget(self.newwords_2, 1, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.EditTransFrame, 0, 0, 1, 1)
        self.EditorChannelsTab.addTab(self.tab_8, "")
        self.gridLayout_6.addWidget(self.EditorChannelsTab, 1, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RenderedChannelTabs = QtWidgets.QTabWidget(self.tab2)
        self.RenderedChannelTabs.setObjectName("RenderedChannelTabs")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.NewTransFrame = QtWidgets.QFrame(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewTransFrame.sizePolicy().hasHeightForWidth())
        self.NewTransFrame.setSizePolicy(sizePolicy)
        self.NewTransFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NewTransFrame.setAutoFillBackground(True)
        self.NewTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.NewTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NewTransFrame.setObjectName("NewTransFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.NewTransFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.newspec_plot = QtWidgets.QWidget(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newspec_plot.sizePolicy().hasHeightForWidth())
        self.newspec_plot.setSizePolicy(sizePolicy)
        self.newspec_plot.setObjectName("newspec_plot")
        self.gridLayout_4.addWidget(self.newspec_plot, 2, 0, 1, 2)
        self.NewSpecScrollBar = QtWidgets.QScrollBar(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewSpecScrollBar.sizePolicy().hasHeightForWidth())
        self.NewSpecScrollBar.setSizePolicy(sizePolicy)
        self.NewSpecScrollBar.setMaximumSize(QtCore.QSize(16777215, 200))
        self.NewSpecScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.NewSpecScrollBar.setObjectName("NewSpecScrollBar")
        self.gridLayout_4.addWidget(self.NewSpecScrollBar, 3, 0, 1, 2)
        self.SetOriginalButton = QtWidgets.QPushButton(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SetOriginalButton.sizePolicy().hasHeightForWidth())
        self.SetOriginalButton.setSizePolicy(sizePolicy)
        self.SetOriginalButton.setIconSize(QtCore.QSize(18, 18))
        self.SetOriginalButton.setObjectName("SetOriginalButton")
        self.gridLayout_4.addWidget(self.SetOriginalButton, 0, 1, 1, 1)
        self.newwords = QtWidgets.QTextEdit(self.NewTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newwords.sizePolicy().hasHeightForWidth())
        self.newwords.setSizePolicy(sizePolicy)
        self.newwords.setObjectName("newwords")
        self.gridLayout_4.addWidget(self.newwords, 1, 0, 1, 2)
        self.gridLayout_11.addWidget(self.NewTransFrame, 0, 0, 1, 1)
        self.RenderedChannelTabs.addTab(self.tab_6, "")
        self.gridLayout_5.addWidget(self.RenderedChannelTabs, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab2, "")
        self.gridLayout.addWidget(self.TabWidget, 0, 0, 1, 1)

        self.retranslateUi(TranscriptEditor)
        self.TabWidget.setCurrentIndex(1)
        self.OriginalChannelTabs.setCurrentIndex(0)
        self.EditorChannelsTab.setCurrentIndex(0)
        self.RenderedChannelTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranscriptEditor)

    def retranslateUi(self, TranscriptEditor):
        _translate = QtCore.QCoreApplication.translate
        TranscriptEditor.setWindowTitle(_translate("TranscriptEditor", "Dialog"))
        self.OriginalChannelTabs.setTabText(self.OriginalChannelTabs.indexOf(self.tab_2), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TranscriptEditor", "Original Transcription"))
        self.RenderButton.setText(_translate("TranscriptEditor", "Render"))
        self.EditorChannelsTab.setTabText(self.EditorChannelsTab.indexOf(self.tab_8), _translate("TranscriptEditor", "Channel 1"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("TranscriptEditor", "Transcript Editor"))
        self.SetOriginalButton.setText(_translate("TranscriptEditor", "Set as Original"))
        self.RenderedChannelTabs.setTabText(self.RenderedChannelTabs.indexOf(self.tab_6), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("TranscriptEditor", "Rendered Transcription"))


    ### ADD CUSTOM FUNCTIONS BELOW THIS LINE AUTO GENERATED ABOVE ###

    # Called after Render button
    # Need to add audio file things eventually maybe
    def doRender(self):
        self.readTranscripts()

        render = self.oldTranscripts[self.numchannels - 1].RenderTranscription(self.oldTranscripts[self.numchannels - 1], self.newTranscripts[self.numchannels - 1], True)
        for i in range(self.numchannels - 1):
            newrender = self.oldTranscripts[i].RenderTranscription(self.oldTranscripts[i], self.newTranscripts[i], True)
            # pad to length
            if(len(newrender) > len(render)):
                render = np.hstack((render, np.zeros(len(newrender) - len(render))))
            elif(len(render) > len(newrender)):
                newrender = np.hstack((newrender, np.zeros(len(render) - len(newrender))))

            render += newrender
        
        print('Rendered, check next tab') 

        spec = stft(input_sound=render, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
        t,f = FormatAxis(spec, self.oldTranscripts[0].sr, len(render)/self.oldTranscripts[0].sr)
        self.plotNewSpec(spec, t, f)

        for i in range(self.numchannels):
            self.newTranscripts[i].quicksort()
        
        maintrans = Transcript()
        maintrans.MainFromOthers(self.newTranscripts)
        self.setNewTranscriptText(maintrans)

        sound(render, self.newTranscripts[0].sr, 'Rendered Sound')

    # reads the new timestamps and sets the values
    def readTranscripts(self):
        self.newTranscripts = [0] * self.numchannels

        for c in range(self.numchannels):
            self.newTranscripts[c] = Transcript()
            self.newTranscripts[c].copyother(self.oldTranscripts[c])
            frame = self.editorChannelArray[c]

            text = frame.newwords_2.toPlainText()

            i = 0 
            # parse text, VERY BAD AND WIP
            for idx in range(len(text)-1):
                if(text[idx] == '[' and text[idx+1] == '('):
                    word = self.oldTranscripts[c].words[i]

                    # read new word
                    p = 0
                    newword = ""

                    while text[idx + 6 + p] != ',' :
                        newword += text[idx + 6 + p]
                        p += 1 
                    offset = 8+p
                    self.newTranscripts[c].words[i] = newword

                    #  Parse numbers, very rough since format isnt decided
                    j = 0
                    while text[idx+offset + j] != ',':                 
                        j += 1

                    start = float(text[idx+offset : idx+offset+j])
                    offset += j + 2

                    j = 0
                    while text[idx+offset + j] != ']':                 
                        j += 1

                    end = float(text[idx+offset: idx+offset+j])

                    self.newTranscripts[c].words[i] = word
                    self.newTranscripts[c].timestamps[i] = (start, end)

                    i+=1
                    idx += offset + 8


    def plotNewSpec(self, spec, t, f):

        if(self.newSpecLayer.count() > 0):
            self.newSpecLayer.removeWidget(self.newSpecWidget)

        m = MplCanvas(self.newspec_plot, width=5, height=4)
        m.plotSpec(spec, t, f)
        self.newSpecWidget = m

        self.newSpecLayer.addWidget(m)

        self.show()
        
    # 0 = main, 1-any = channel # 
    def plotOldSpec(self, transcripts, channel):
        if(channel == 0):
            l = QtWidgets.QVBoxLayout(self.oldspec_plot)
            if(l.count() > 0):
                l.removeWidget(self.oldSpecWidget)

            m = MplCanvas(self.oldspec_plot, width=5, height=4)

            render = self.oldTranscripts[self.numchannels-1].audio
            for i in range(self.numchannels - 1):
                newrender = self.oldTranscripts[i].audio
                if(len(newrender) > len(render)):
                    render = np.hstack((render, np.zeros(len(newrender) - len(render))))
                render += newrender

            spec = stft(input_sound=render, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
            t,f = FormatAxis(spec, self.oldTranscripts[0].sr, len(render)/self.oldTranscripts[0].sr)

            m.plotSpec(spec, t, f)
            self.oldSpecWidget = m
            l.addWidget(m)
            self.show()

        if(channel > 0):
            frame = self.oldChannelArray[channel-1]
            l = QtWidgets.QVBoxLayout(frame.oldspec_plot)

            if(l.count() > 0):
                l.removeWidget(frame.oldSpecWidget)
            m = MplCanvas(frame.oldspec_plot, width=5, height=4)

            spec, t, f = self.oldTranscripts[channel-1].getSpec()
            m.plotSpec(spec, t, f)
            frame.oldSpecWidget = m
            l.addWidget(m)
            self.show()


    #param: words - transcript.words array
    def setOldTranscriptText(self, transcripts, numchannels):
        self.oldTranscripts = []
        # fills in main, This needs to be redone to include all transcripts
        transcript = Transcript()
        transcript.MainFromOthers(transcripts)
        text = ""
        words = transcript.words
        times = transcript.timestamps
        for i in range(len(words)):
            text += words[i] + ' ' 
        self.oldwords.setText(text)
        self.oldTranscripts.append(transcripts[0])

        # create new tabs and fill in
        if(numchannels > 1):
            # create new tabs for each channel and add its transcription
            # aarray holds frames
            self.oldChannelArray = []
            self.oldTranscripts = []
            for i in range(numchannels):
                # duplicate frame, create new tab and place
                tabname = "Channel " + str(i+1)
    
                newtab = QtWidgets.QWidget()
                newframe = TranscriptPlotFrame(self.OriginalChannelTabs)
                newframe.setupUi(newframe)

                gridlayout = QtWidgets.QGridLayout(newtab)
                gridlayout.addWidget(newframe, 0, 0, 1, 1)
                
                # TODO, fix layout to grid !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              

                self.OriginalChannelTabs.addTab(newtab, tabname) 
                self.oldChannelArray.append(newframe)

                # setup words  
                transcript = transcripts[i]    

                text = ""
                words = transcript.words
                times = transcript.timestamps
                for k in range(len(words)):
                    text += words[k] + ' ' 

                newframe.oldwords.setText(text)
                self.oldTranscripts.append(transcripts[i])
                

        
        self.OriginalChannelTabs.setCurrentIndex(0)


    ## happens only when original transcription is set and on first transcript
    def initTranscriptEditor(self, transcripts, numchannels):
        self.editorChannelArray = []

        for j in range(self.EditorChannelsTab.count()):
            self.EditorChannelsTab.removeTab(j)

        for i in range(numchannels):
            tabname = "Channel " + str(i+1)
            newtab = QtWidgets.QWidget()
            newframe = TranscriptEditorFrame(self.EditorChannelsTab)
            newframe.setupUi(newframe)

            gridlayout = QtWidgets.QGridLayout(newtab)
            gridlayout.addWidget(newframe, 0, 0, 1, 1)

            self.EditorChannelsTab.addTab(newtab, tabname)
            self.editorChannelArray.append(newframe)

            transcript = transcripts[i]
            text = ""
            words = transcript.words
            times = transcript.timestamps
            for i in range(len(words)):
                text += '[(' + str(i) + '), ' + words[i] + ', ' + str(times[i][0]) + ', ' + str(times[i][1]) + ' ]  \n'

            newframe.textBrowser.setPlaceholderText('[(word #), word, start_time, end_time], (WIP) DONT EDIT WORD NUMBERS AND WORDS')
            newframe.newwords_2.setText(text)


    def setNewTranscriptText(self, transcript):
        # TODO, Main channels should show all words of each channel
        text = ""
        words = transcript.words
        times = transcript.timestamps
        for i in range(len(words)):
            text += words[i] + ' '  
        
        self.newwords.setText(text)


    def clearLayout(self, layout):
      while layout.count():
        child = layout.takeAt(0)
        if child.widget():
          child.widget().deleteLater()

    ## for hooking up buttons and stuff keep at bottom for function reading
    def setupUiManual(self):
        self.RenderButton.clicked.connect(self.doRender)
        self.newSpecLayer = QtWidgets.QVBoxLayout(self.newspec_plot) 
        #self.oldSpecLayer = QtWidgets.QVBoxLayout(self.oldspec_plot)

        
        self.TabWidget.setFocus()
        self.setCentralWidget(self.TabWidget)
    
    # transcripts = array of transcripts, len(transcripts) = number of channels
    def launchInit(self,transcripts, numchannels):
        self.numchannels = numchannels
        self.setOldTranscriptText(transcripts, numchannels)
        for i in range(numchannels+1):
            self.plotOldSpec(transcripts, i)
        self.initTranscriptEditor(transcripts, numchannels)


## matplotlib canvas widget class thing
class MplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

    def plotSpec(self, spec, t, f):
        self.axes.clear()
        self.axes.cla()
        self.axes.pcolormesh(t, f, abs(spec)**0.3) # n^0.3 to 'normalize' 
        self.axes.set_xlabel('time (seconds)')
        self.axes.set_ylabel('Frequency (Hz)')
        self.draw()

    ### just to test plot ####
    def plotexample(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranscriptEditor = QtWidgets.QDialog()
    ui = Ui_TranscriptEditor()
    ui.setupUi(TranscriptEditor)
    TranscriptEditor.show()
    sys.exit(app.exec_())


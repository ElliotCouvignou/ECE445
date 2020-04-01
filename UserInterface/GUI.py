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
import copy

from TranscriptPlotTab import TranscriptPlotFrame   
from TranscriptEditorTab import TranscriptEditorFrame
from Render import Transcript, RenderSettings
from DSP import stft, FormatAxis, sound


class Ui_TranscriptEditor(QMainWindow):
    def setupUi(self, TranscriptEditor):
        TranscriptEditor.setObjectName("TranscriptEditor")
        TranscriptEditor.resize(1220, 799)
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
        self.textBrowser.setTabStopDistance(88.0)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.EditTransFrame, 0, 0, 1, 1)
        self.EditorChannelsTab.addTab(self.tab_8, "")
        self.gridLayout_6.addWidget(self.EditorChannelsTab, 1, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.RenderSettingsFrame = QtWidgets.QFrame(self.tab_3)
        self.RenderSettingsFrame.setGeometry(QtCore.QRect(10, 20, 1141, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderSettingsFrame.sizePolicy().hasHeightForWidth())
        self.RenderSettingsFrame.setSizePolicy(sizePolicy)
        self.RenderSettingsFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RenderSettingsFrame.setAutoFillBackground(True)
        self.RenderSettingsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.RenderSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RenderSettingsFrame.setObjectName("RenderSettingsFrame")
        self.PauseShorteningFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.PauseShorteningFrame.setGeometry(QtCore.QRect(12, 12, 341, 131))
        self.PauseShorteningFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PauseShorteningFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PauseShorteningFrame.setObjectName("PauseShorteningFrame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.PauseShorteningFrame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PauseShorteningText = QtWidgets.QTextEdit(self.PauseShorteningFrame)
        self.PauseShorteningText.setObjectName("PauseShorteningText")
        self.gridLayout_10.addWidget(self.PauseShorteningText, 0, 0, 1, 1)
        self.PauseShorteningButton = QtWidgets.QRadioButton(self.PauseShorteningFrame)
        self.PauseShorteningButton.setChecked(False)
        self.PauseShorteningButton.setObjectName("PauseShorteningButton")
        self.gridLayout_10.addWidget(self.PauseShorteningButton, 1, 0, 1, 1)
        self.PauseShortenAmountBox = QtWidgets.QDoubleSpinBox(self.PauseShorteningFrame)
        self.PauseShortenAmountBox.setObjectName("PauseShortenAmountBox")
        self.gridLayout_10.addWidget(self.PauseShortenAmountBox, 2, 0, 1, 1)
        self.BackgrundNoiseFillFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.BackgrundNoiseFillFrame.setGeometry(QtCore.QRect(360, 10, 241, 121))
        self.BackgrundNoiseFillFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackgrundNoiseFillFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackgrundNoiseFillFrame.setObjectName("BackgrundNoiseFillFrame")
        self.BackGroundNoiseFillerText = QtWidgets.QTextEdit(self.BackgrundNoiseFillFrame)
        self.BackGroundNoiseFillerText.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.BackGroundNoiseFillerText.setObjectName("BackGroundNoiseFillerText")
        self.BackgroundNoiseFillButton = QtWidgets.QRadioButton(self.BackgrundNoiseFillFrame)
        self.BackgroundNoiseFillButton.setGeometry(QtCore.QRect(10, 60, 191, 19))
        self.BackgroundNoiseFillButton.setObjectName("BackgroundNoiseFillButton")
        self.WindowingEnableFrame = QtWidgets.QFrame(self.RenderSettingsFrame)
        self.WindowingEnableFrame.setGeometry(QtCore.QRect(610, 10, 291, 81))
        self.WindowingEnableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowingEnableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowingEnableFrame.setObjectName("WindowingEnableFrame")
        self.CrossfadeEnableText = QtWidgets.QTextEdit(self.WindowingEnableFrame)
        self.CrossfadeEnableText.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.CrossfadeEnableText.setObjectName("CrossfadeEnableText")
        self.CrossfadeEnableButton = QtWidgets.QRadioButton(self.WindowingEnableFrame)
        self.CrossfadeEnableButton.setGeometry(QtCore.QRect(10, 50, 231, 19))
        self.CrossfadeEnableButton.setObjectName("CrossfadeEnableButton")
        self.TabWidget.addTab(self.tab_3, "")
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
        self.TabWidget.setCurrentIndex(0)
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
        self.PauseShorteningText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pause Shortening:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter max pause amount in slider. Any pauses &gt; amount gets shortened to amount</p></body></html>"))
        self.PauseShorteningButton.setText(_translate("TranscriptEditor", "Enable Pause Shorterning"))
        self.BackGroundNoiseFillerText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Background Noise Filler:</span></p></body></html>"))
        self.BackgroundNoiseFillButton.setText(_translate("TranscriptEditor", "Enable Background Noise Filler"))
        self.CrossfadeEnableText.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Crossfade start/ends of sliced semgents:</span></p></body></html>"))
        self.CrossfadeEnableButton.setText(_translate("TranscriptEditor", "Enable Crossfade on edited segments"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_3), _translate("TranscriptEditor", "Render Settings"))
        self.SetOriginalButton.setText(_translate("TranscriptEditor", "Set as Original"))
        self.RenderedChannelTabs.setTabText(self.RenderedChannelTabs.indexOf(self.tab_6), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("TranscriptEditor", "Rendered Transcription"))


    ### ADD CUSTOM FUNCTIONS BELOW THIS LINE AUTO GENERATED ABOVE ###

    # Called after Render button
    # Need to add audio file things eventually maybe
    def doRender(self):
        # read rendersettings to send as render parameter
        rendersettings = self.readRenderSettings()

        # setup to find overlap
        if(rendersettings.pauseShortenEnable):
            for i in range(self.numchannels):
                self.oldTranscripts[i].findPauses()
            self.oldTranscripts[0].findOverlappingPauses(self.oldTranscripts, rendersettings)

        render = self.oldTranscripts[self.numchannels - 1].RenderTranscription(self.oldTranscripts[self.numchannels - 1], rendersettings)
        for i in range(self.numchannels - 1):
            newrender = self.oldTranscripts[i].RenderTranscription(self.oldTranscripts[i], rendersettings)
            # pad to length w/Stereo/Mono checks
            if(newrender.shape[1] > render.shape[1]):
                if(render.shape[0] == 2):
                    pad = newrender.shape[1] - render.shape[1]
                    render = np.hstack((render, np.zeros(pad*2).reshape(2,pad)))
                else:
                    render = np.hstack((render, np.zeros(newrender.shape[1] - render.shape[1])))
            elif(newrender.shape[1] < render.shape[1]):
                if(render.shape[0] == 2):
                    pad = render.shape[1] - newrender.shape[1]
                    newrender= np.hstack((newrender, np.zeros(pad*2).reshape(2,pad)))
                else:
                    newrender = np.hstack((newrender, np.zeros(render.shape[1] - newrender.shape[1])))

            render += newrender
        
        print('Rendered, check next tab') 
        #flatten to mono for spectrogram (resulting audio isnt flattened)
        if(render.shape[0] > 1):
            ins = render.sum(axis=0) / 2
            f, t, spec = signal.spectrogram(ins.transpose(), self.oldTranscripts[0].sr)
        else:
            f, t, spec = signal.spectrogram(render, self.oldTranscripts[0].sr)
        

        #spec = stft(input_sound=render, dft_size=256, hop_size=64, zero_pad=256, window=signal.hann(256))
        #t,f = FormatAxis(spec, self.oldTranscripts[0].sr, len(render)/self.oldTranscripts[0].sr)
        self.plotNewSpec(spec, t, f)

        for i in range(self.numchannels):
            self.oldTranscripts[i].quicksort( (0, len(self.oldTranscripts[i].timestamps) - 1) )
        
        maintrans = Transcript()
        maintrans.MainFromOthers(self.oldTranscripts)
        self.setNewTranscriptText(maintrans)

        sound(render, self.oldTranscripts[0].sr, 'Rendered Sound')

    # creates a RenderSettings class and fills out parameters based on user inputs
    def readRenderSettings(self):
        rendersettings = RenderSettings()
        # just go through rendersettings tab
        rendersettings.pauseShortenEnable = self.PauseShorteningButton.isChecked()
        rendersettings.pauseShortenAmount = self.PauseShortenAmountBox.value()
        rendersettings.backgroundFillEnable = self.BackgroundNoiseFillButton.isChecked()
        rendersettings.crossfadeEnable = self.CrossfadeEnableButton.isChecked()
        #print('readsettigns: ', rendersettings.pauseShortenEnable, rendersettings.pauseShortenAmount, rendersettings.backgroundFillEnable)

        return rendersettings

    # function for when Apply Shift button is pressed in the transcript editor
    def doApplyShift(self):        
        #get active/visible editor tab
        activeIdx = self.EditorChannelsTab.currentIndex()
        activeWidget =  self.editorChannelArray[activeIdx]
        activeTranscript = self.oldTranscripts[activeIdx]

        # do nothing check
        if(activeWidget.WordShiftAmount.value() == 0 and activeWidget.WordSelectEnd.value() == 0):
            return 

        # get select idx, -1 to convert to 0 index
        selectstart = max(activeWidget.WordSelectStart.value()-1, 0)
        
        selectend = min(activeWidget.WordSelectEnd.value()-1, activeTranscript.wordCount -1) 
        if(selectend == -1):
            selectend = activeTranscript.wordCount -1
        shiftamt = activeWidget.WordShiftAmount.value()

        # quick check to make sure we cant shift into negative times, if this happends then move 
        # earliest word to 0.00
        if(activeTranscript.timestamps[selectstart][0] + shiftamt < 0):
            shiftamt = -activeTranscript.timestamps[selectstart][0]

        # apply shift to timestamps and keep track of shifts in shift array
        i = selectstart
        end = min(activeTranscript.audiolength, selectend)
        while i <= end:
            tup = activeTranscript.timestamps[i]
            activeTranscript.timestamps[i] = (tup[0] + shiftamt, tup[1] + shiftamt)
            activeTranscript.shifts[i] += shiftamt
            i += 1
        
        activeWidget.WordSelectEnd.setValue(0)
        activeWidget.WordSelectStart.setValue(0)
        activeWidget.WordShiftAmount.setValue(0.00)

        print('shift applied')
        

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
            
            # mono/stero handle
            if(self.oldTranscripts[self.numchannels-1].isStereo):
                render = self.oldTranscripts[self.numchannels-1].audio.sum(axis=1) / 2
            else:
                render = copy.deepcopy(self.oldTranscripts[self.numchannels-1].audio)
            for i in range(self.numchannels - 1):
                # mono/stero handle
                if(self.oldTranscripts[i].isStereo):
                    newrender = self.oldTranscripts[i].audio.sum(axis=1) / 2
                else:
                    newrender = self.oldTranscripts[i].audio

                # combine renders
                if(len(newrender) > len(render)):
                    render = np.hstack((render, np.zeros(len(newrender) - len(render))))
                render = np.add(newrender, render)

            f, t, spec = signal.spectrogram(render, self.oldTranscripts[0].sr)

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
        for i in range(len(words)):
            text += words[i] + ' ' 
        self.oldwords.setText(text)
        self.oldTranscripts.append(transcripts[0])

        # create new tabs and fill in
        if(numchannels >= 1):
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

        for t in range(numchannels):
            tabname = "Channel " + str(t+1)
            newtab = QtWidgets.QWidget()
            newframe = TranscriptEditorFrame(self.EditorChannelsTab)
            newframe.setupUi(newframe)

            gridlayout = QtWidgets.QGridLayout(newtab)
            gridlayout.addWidget(newframe, 0, 0, 1, 1)

            self.EditorChannelsTab.addTab(newtab, tabname)
            self.editorChannelArray.append(newframe)

            transcript = transcripts[t]
            text = ""
            words = transcript.words
            times = transcript.timestamps
            wordslength = len(words)
            for i in range(len(words)):
                if(i%10 == 0):
                    # word segment and timestamp labeling
                    if(i!=0):
                        text+='\n'
                    text += '[' + str(i+1) + ' - ' + str(min(i+10, wordslength)) + '] '
                    text += '(' + str(times[i][0]) + ' - ' + str(times[min(i+9, wordslength-1)][1]) + '): '
                text += words[i] + ' '

            newframe.DescriptionBox.setText('Word select index start (0 = start of transcript): \nWord select index end (0 = end of transcript): \nWord shift amount (seconds):\n [word# start, Word# End] (section starttime, section endtime)')
            newframe.TranscriptWordBox.setText(text)

            # link apply shift button to our function
            newframe.ApplyShiftButton.clicked.connect(self.doApplyShift)

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


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

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from Render import RenderCall, Transcript


class Ui_TranscriptEditor(QMainWindow):
    def setupUi(self, TranscriptEditor):
        TranscriptEditor.setObjectName("TranscriptEditor")
        TranscriptEditor.resize(1134, 653)
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
        self.TabWidget.setAutoFillBackground(True)
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.OldTransFrame = QtWidgets.QFrame(self.tab1)
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
        self.gridLayout_2.addWidget(self.OldTransFrame, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 1)
        self.EditTransFrame = QtWidgets.QFrame(self.tab)
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
        self.RenderButton = QtWidgets.QPushButton(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderButton.sizePolicy().hasHeightForWidth())
        self.RenderButton.setSizePolicy(sizePolicy)
        self.RenderButton.setIconSize(QtCore.QSize(18, 18))
        self.RenderButton.setObjectName("RenderButton")
        self.gridLayout_7.addWidget(self.RenderButton, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.EditTransFrame, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.NewTransFrame = QtWidgets.QFrame(self.tab2)
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
        self.gridLayout_5.addWidget(self.NewTransFrame, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab2, "")
        self.gridLayout.addWidget(self.TabWidget, 0, 0, 1, 1)

        self.retranslateUi(TranscriptEditor)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranscriptEditor)
        
        self.TabWidget.setFocus()
        self.setCentralWidget(self.TabWidget)

    def retranslateUi(self, TranscriptEditor):
        _translate = QtCore.QCoreApplication.translate
        TranscriptEditor.setWindowTitle(_translate("TranscriptEditor", "Dialog"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TranscriptEditor", "Original Transcription"))
        self.RenderButton.setText(_translate("TranscriptEditor", "Render"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("TranscriptEditor", "Transcript Editor"))
        self.SetOriginalButton.setText(_translate("TranscriptEditor", "Set as Original"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("TranscriptEditor", "Rendered Transcription"))

    ### ADD CUSTOM FUNCTIONS BELOW THIS LINE AUTO GENERATED ABOVE ###

    # Called after Render button
    # Need to add audio file things eventually maybe
    def doRender(self):
        self.readTranscript()
        self.textBrowser.setPlaceholderText('pepepepepeppe') 
        RenderCall(self.oldTranscript, self.newTranscript)

    # reads the new timestamps and sets the values
    def readTranscript(self):
        self.newTranscript = Transcript()
        self.newTranscript.copyother(self.oldTranscript)

        text = self.newwords_2.toPlainText()
        
        i = 0 
        # parse text, VERY BAD AND WIP
        for idx in range(len(text)-1):
            if(text[idx] == '[' and text[idx+1] == '('):
                word = self.oldTranscript.words[i]

                # read new word
                p = 0
                while text[idx + 5 + p] != ' ':
                    print('ed: ', text[p])
                    p += 1 
                newword = text[idx+5 : idx+5+p]
                offset = 7+p
                self.newTranscript.words[i] = newword
                
                #  ASSUMING ONLY 1 DECIMAL PLACE
                start = text[offset:offset+2]
                end = text[offset+4:offset+6]
                self.newTranscript.timestamps[i] = (start,end)

                i+=1
        

    def plotOldSpec(self, spec, t, f):
        l = QtWidgets.QVBoxLayout(self.oldspec_plot)

        m = MplCanvas(self.oldspec_plot, width=5, height=4)
        m.plotOldSpec(spec, t, f)
        m.move(0,0)

        l.addWidget(m)

        self.show()

    #param: words - transcript.words array
    def setTranscriptText(self, transcript):
        text = ""
        words = transcript.words
        times = transcript.timestamps
        for i in range(len(words)):
            text += words[i] + ' ' 
        
        self.oldwords.setText(text)

    ## happens only when original transcription is set and on first transcript
    def initTranscriptEditor(self, transcript):
        self.oldTranscript = transcript

        text = ""
        words = transcript.words
        times = transcript.timestamps
        for i in range(len(words)):
            text += '[(' + str(i) + '), ' + words[i] + ', ' + str(times[i][0]) + ', ' + str(times[i][1]) + ' ]  \n'
        
        self.textBrowser.setPlaceholderText('[(word #), word, start_time, end_time], (WIP) DONT EDIT WORD NUMBERS AND WORDS')
        self.newwords_2.setText(text)

    ## for hooking up buttons and stuff keep at bottom for function reading
    def setupUiManual(self):
        self.RenderButton.clicked.connect(self.doRender)


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

    def plotOldSpec(self, spec, t, f):
        self.axes.cla()
        self.axes.pcolormesh(t, f, abs(spec)**0.3) # n^0.3 to 'normalize' 
        self.axes.set_title('Raw Audio Spectrogram')
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


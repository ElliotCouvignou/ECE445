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


class Ui_TranscriptEditor(QMainWindow):
    def setupUi(self, TranscriptEditor):
        TranscriptEditor.setObjectName("TranscriptEditor")
        TranscriptEditor.resize(1100, 735)
        self.TabWidget = QtWidgets.QTabWidget(TranscriptEditor)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 1041, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        self.TabWidget.setAutoFillBackground(True)
        self.TabWidget.setObjectName("TabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.OldTransFrame = QtWidgets.QFrame(self.tab1)
        self.OldTransFrame.setGeometry(QtCore.QRect(0, 0, 1031, 441))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldTransFrame.sizePolicy().hasHeightForWidth())
        self.OldTransFrame.setSizePolicy(sizePolicy)
        self.OldTransFrame.setAutoFillBackground(True)
        self.OldTransFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.OldTransFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OldTransFrame.setObjectName("OldTransFrame")
        self.OriginalTranscript_t = QtWidgets.QTextBrowser(self.OldTransFrame)
        self.OriginalTranscript_t.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.OriginalTranscript_t.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OriginalTranscript_t.setObjectName("OriginalTranscript_t")
        self.oldwords = QtWidgets.QTextEdit(self.OldTransFrame)
        self.oldwords.setGeometry(QtCore.QRect(20, 50, 961, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldwords.sizePolicy().hasHeightForWidth())
        self.oldwords.setSizePolicy(sizePolicy)
        self.oldwords.setObjectName("oldwords")
        self.OldSpecScrollBar = QtWidgets.QScrollBar(self.OldTransFrame)
        self.OldSpecScrollBar.setGeometry(QtCore.QRect(20, 420, 961, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OldSpecScrollBar.sizePolicy().hasHeightForWidth())
        self.OldSpecScrollBar.setSizePolicy(sizePolicy)
        self.OldSpecScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.OldSpecScrollBar.setObjectName("OldSpecScrollBar")
        self.oldspec_plot = QtWidgets.QWidget(self.OldTransFrame)
        self.oldspec_plot.setGeometry(QtCore.QRect(20, 110, 961, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oldspec_plot.sizePolicy().hasHeightForWidth())
        self.oldspec_plot.setSizePolicy(sizePolicy)
        self.oldspec_plot.setObjectName("oldspec_plot")
        self.TabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.TabWidget.addTab(self.tab2, "")

        self.retranslateUi(TranscriptEditor)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranscriptEditor)

        self.plot = self.oldspec_plot

        self.TabWidget.setFocus()
        self.setCentralWidget(self.TabWidget)

    def retranslateUi(self, TranscriptEditor):
        _translate = QtCore.QCoreApplication.translate
        TranscriptEditor.setWindowTitle(_translate("TranscriptEditor", "Dialog"))
        self.OriginalTranscript_t.setPlaceholderText(_translate("TranscriptEditor", "Original Transcript:"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TranscriptEditor", "Tab 1"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab2), _translate("TranscriptEditor", "Tab 2"))

    ### ADD CUSTOM FUNCTIONS BELOW THIS LINE AUTO GENERATED ABOVE ###

    def plotOldSpec(self):
        l = QtWidgets.QVBoxLayout(self.plot)

        m = MplCanvas(self.plot, width=5, height=4)
        m.plot()
        m.move(0,0)

        l.addWidget(m)

        self.show()

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


    def plot(self):
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


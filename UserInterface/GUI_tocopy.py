# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranscriptEditor(object):
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
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.EditTransFrame = QtWidgets.QFrame(self.frame_2)
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
        self.ChannelSelectBox = QtWidgets.QSpinBox(self.EditTransFrame)
        self.ChannelSelectBox.setMaximum(0)
        self.ChannelSelectBox.setObjectName("ChannelSelectBox")
        self.gridLayout_7.addWidget(self.ChannelSelectBox, 0, 1, 1, 1)
        self.WordShiftAmount = QtWidgets.QDoubleSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordShiftAmount.sizePolicy().hasHeightForWidth())
        self.WordShiftAmount.setSizePolicy(sizePolicy)
        self.WordShiftAmount.setMinimum(-9999999.0)
        self.WordShiftAmount.setMaximum(9999999.0)
        self.WordShiftAmount.setObjectName("WordShiftAmount")
        self.gridLayout_7.addWidget(self.WordShiftAmount, 3, 1, 1, 1)
        self.ApplyShiftButton = QtWidgets.QPushButton(self.EditTransFrame)
        self.ApplyShiftButton.setObjectName("ApplyShiftButton")
        self.gridLayout_7.addWidget(self.ApplyShiftButton, 4, 1, 1, 1)
        self.WordSelectStart = QtWidgets.QSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordSelectStart.sizePolicy().hasHeightForWidth())
        self.WordSelectStart.setSizePolicy(sizePolicy)
        self.WordSelectStart.setObjectName("WordSelectStart")
        self.gridLayout_7.addWidget(self.WordSelectStart, 1, 1, 1, 1)
        self.WordSelectEnd = QtWidgets.QSpinBox(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WordSelectEnd.sizePolicy().hasHeightForWidth())
        self.WordSelectEnd.setSizePolicy(sizePolicy)
        self.WordSelectEnd.setObjectName("WordSelectEnd")
        self.gridLayout_7.addWidget(self.WordSelectEnd, 2, 1, 1, 1)
        self.TranscriptWordBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TranscriptWordBox.sizePolicy().hasHeightForWidth())
        self.TranscriptWordBox.setSizePolicy(sizePolicy)
        self.TranscriptWordBox.setTabStopDistance(88.0)
        self.TranscriptWordBox.setPlaceholderText("")
        self.TranscriptWordBox.setObjectName("TranscriptWordBox")
        self.gridLayout_7.addWidget(self.TranscriptWordBox, 6, 0, 1, 2)
        self.RenderButton = QtWidgets.QPushButton(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RenderButton.sizePolicy().hasHeightForWidth())
        self.RenderButton.setSizePolicy(sizePolicy)
        self.RenderButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.RenderButton.setIconSize(QtCore.QSize(18, 18))
        self.RenderButton.setObjectName("RenderButton")
        self.gridLayout_7.addWidget(self.RenderButton, 5, 1, 1, 1)
        self.DescriptionBox = QtWidgets.QTextBrowser(self.EditTransFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionBox.sizePolicy().hasHeightForWidth())
        self.DescriptionBox.setSizePolicy(sizePolicy)
        self.DescriptionBox.setObjectName("DescriptionBox")
        self.gridLayout_7.addWidget(self.DescriptionBox, 0, 0, 6, 1)
        self.gridLayout_9.addWidget(self.EditTransFrame, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.RenderSettingsFrame = QtWidgets.QFrame(self.tab_3)
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
        self.gridLayout_12.addWidget(self.RenderSettingsFrame, 0, 0, 1, 1)
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
        self.RenderedChannelTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TranscriptEditor)

    def retranslateUi(self, TranscriptEditor):
        _translate = QtCore.QCoreApplication.translate
        TranscriptEditor.setWindowTitle(_translate("TranscriptEditor", "Dialog"))
        self.OriginalChannelTabs.setTabText(self.OriginalChannelTabs.indexOf(self.tab_2), _translate("TranscriptEditor", "Main Channel"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), _translate("TranscriptEditor", "Original Transcription"))
        self.ApplyShiftButton.setText(_translate("TranscriptEditor", "Apply Shift"))
        self.RenderButton.setText(_translate("TranscriptEditor", "Render"))
        self.DescriptionBox.setHtml(_translate("TranscriptEditor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Speaker number selection:</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Word selection starting index:</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Word selection ending index:</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Word segment shift amount (seconds):</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Format of transcript:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speaker #&lt;channel number&gt;: [ &lt;first word index&gt;, &lt;timestamp of first word&gt;]   word, next word, next next word, ... [ &lt;last word index&gt;, &lt;timestamp of last word&gt;]</p></body></html>"))
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

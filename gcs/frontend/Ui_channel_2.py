# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_channel_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_channel_2(object):
    def setupUi(self, channel_2):
        channel_2.setObjectName("channel_2")
        channel_2.resize(825, 510)
        self.frame = QtWidgets.QFrame(channel_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 231, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.splitter = QtWidgets.QSplitter(self.frame)
        self.splitter.setGeometry(QtCore.QRect(0, 50, 231, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = channel_widget(self.splitter)
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_channel_number = QtWidgets.QLabel(self.layoutWidget)
        self.label_channel_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channel_number.setObjectName("label_channel_number")
        self.verticalLayout.addWidget(self.label_channel_number)
        self.label_description = QtWidgets.QLabel(self.layoutWidget)
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)

        self.retranslateUi(channel_2)
        QtCore.QMetaObject.connectSlotsByName(channel_2)

    def retranslateUi(self, channel_2):
        _translate = QtCore.QCoreApplication.translate
        channel_2.setWindowTitle(_translate("channel_2", "Form"))
        self.label_channel_number.setText(_translate("channel_2", "Channel 2"))
        self.label_description.setText(_translate("channel_2", "[Description]"))

from .channel_widget import channel_widget

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_channel_3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_channel_3(object):
    def setupUi(self, channel_3):
        channel_3.setObjectName("channel_3")
        channel_3.resize(234, 267)
        channel_3.setMinimumSize(QtCore.QSize(234, 267))
        channel_3.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(channel_3)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(channel_3)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_channel_number = QtWidgets.QLabel(self.frame)
        self.label_channel_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channel_number.setObjectName("label_channel_number")
        self.verticalLayout.addWidget(self.label_channel_number)
        self.label_description = QtWidgets.QLabel(self.frame)
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.widget = channel_widget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(220, 220))
        self.widget.setMaximumSize(QtCore.QSize(400, 270))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignVCenter)

        self.retranslateUi(channel_3)
        QtCore.QMetaObject.connectSlotsByName(channel_3)

    def retranslateUi(self, channel_3):
        _translate = QtCore.QCoreApplication.translate
        channel_3.setWindowTitle(_translate("channel_3", "Form"))
        self.label_channel_number.setText(_translate("channel_3", "Channel 3"))
        self.label_description.setText(_translate("channel_3", "[Description]"))

from .channel_widget import channel_widget

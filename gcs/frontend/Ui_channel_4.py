# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_channel_4.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_channel_4(object):
    def setupUi(self, channel_4):
        channel_4.setObjectName("channel_4")
        channel_4.resize(234, 267)
        channel_4.setMinimumSize(QtCore.QSize(234, 267))
        channel_4.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(channel_4)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(channel_4)
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

        self.retranslateUi(channel_4)
        QtCore.QMetaObject.connectSlotsByName(channel_4)

    def retranslateUi(self, channel_4):
        _translate = QtCore.QCoreApplication.translate
        channel_4.setWindowTitle(_translate("channel_4", "Form"))
        self.label_channel_number.setText(_translate("channel_4", "Channel 4"))
        self.label_description.setText(_translate("channel_4", "[Description]"))

from .channel_widget import channel_widget

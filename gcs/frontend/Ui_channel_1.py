# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_channel_1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_channel_1(object):
    def setupUi(self, channel_1):
        channel_1.setObjectName("channel_1")
        channel_1.resize(825, 510)
        self.frame = QtWidgets.QFrame(channel_1)
        self.frame.setGeometry(QtCore.QRect(10, 10, 250, 261))
        self.frame.setMinimumSize(QtCore.QSize(250, 260))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_channel_number = QtWidgets.QLabel(self.frame)
        self.label_channel_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_channel_number.setObjectName("label_channel_number")
        self.verticalLayout.addWidget(self.label_channel_number)
        self.label_description = QtWidgets.QLabel(self.frame)
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widget = channel_widget(self.frame)
        self.widget.setMinimumSize(QtCore.QSize(230, 200))
        self.widget.setMaximumSize(QtCore.QSize(400, 200))
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(channel_1)
        QtCore.QMetaObject.connectSlotsByName(channel_1)

    def retranslateUi(self, channel_1):
        _translate = QtCore.QCoreApplication.translate
        channel_1.setWindowTitle(_translate("channel_1", "Form"))
        self.label_channel_number.setText(_translate("channel_1", "Channel 1"))
        self.label_description.setText(_translate("channel_1", "[Description]"))

from .channel_widget import channel_widget

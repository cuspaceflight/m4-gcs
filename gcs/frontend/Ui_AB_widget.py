# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_AB_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AB_widget(object):
    def setupUi(self, AB_widget):
        AB_widget.setObjectName("AB_widget")
        AB_widget.resize(1180, 270)
        AB_widget.setMinimumSize(QtCore.QSize(1180, 270))
        self.horizontalLayout = QtWidgets.QHBoxLayout(AB_widget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chan1 = channel_1(AB_widget)
        self.chan1.setMinimumSize(QtCore.QSize(234, 267))
        self.chan1.setObjectName("chan1")
        self.horizontalLayout.addWidget(self.chan1, 0, QtCore.Qt.AlignVCenter)
        self.chan2 = channel_2(AB_widget)
        self.chan2.setMinimumSize(QtCore.QSize(234, 267))
        self.chan2.setObjectName("chan2")
        self.horizontalLayout.addWidget(self.chan2, 0, QtCore.Qt.AlignVCenter)
        self.chan3 = channel_3(AB_widget)
        self.chan3.setMinimumSize(QtCore.QSize(234, 267))
        self.chan3.setObjectName("chan3")
        self.horizontalLayout.addWidget(self.chan3, 0, QtCore.Qt.AlignVCenter)
        self.chan4 = channel_4(AB_widget)
        self.chan4.setMinimumSize(QtCore.QSize(234, 267))
        self.chan4.setObjectName("chan4")
        self.horizontalLayout.addWidget(self.chan4, 0, QtCore.Qt.AlignVCenter)
        self.chan5 = channel_5(AB_widget)
        self.chan5.setMinimumSize(QtCore.QSize(234, 267))
        self.chan5.setObjectName("chan5")
        self.horizontalLayout.addWidget(self.chan5, 0, QtCore.Qt.AlignVCenter)

        self.retranslateUi(AB_widget)
        QtCore.QMetaObject.connectSlotsByName(AB_widget)

    def retranslateUi(self, AB_widget):
        _translate = QtCore.QCoreApplication.translate
        AB_widget.setWindowTitle(_translate("AB_widget", "Form"))

from .channel_1 import channel_1
from .channel_2 import channel_2
from .channel_3 import channel_3
from .channel_4 import channel_4
from .channel_5 import channel_5

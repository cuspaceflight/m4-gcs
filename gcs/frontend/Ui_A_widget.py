# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_A_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_A_widget(object):
    def setupUi(self, A_widget):
        A_widget.setObjectName("A_widget")
        A_widget.resize(1165, 319)
        self.frame_2 = QtWidgets.QFrame(A_widget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 1521, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = AB_widget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1521, 291))
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()

        self.retranslateUi(A_widget)
        QtCore.QMetaObject.connectSlotsByName(A_widget)

    def retranslateUi(self, A_widget):
        _translate = QtCore.QCoreApplication.translate
        A_widget.setWindowTitle(_translate("A_widget", "Form"))
        self.label.setText(_translate("A_widget", "A"))

from .AB_widget import AB_widget

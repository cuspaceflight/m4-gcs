# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_B_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_B_widget(object):
    def setupUi(self, B_widget):
        B_widget.setObjectName("B_widget")
        B_widget.resize(1600, 354)
        B_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(B_widget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(B_widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.AB_status = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AB_status.setFont(font)
        self.AB_status.setReadOnly(True)
        self.AB_status.setObjectName("AB_status")
        self.gridLayout.addWidget(self.AB_status, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.widget = AB_widget(self.frame_2)
        self.widget.setMinimumSize(QtCore.QSize(1180, 270))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignVCenter)

        self.retranslateUi(B_widget)
        QtCore.QMetaObject.connectSlotsByName(B_widget)

    def retranslateUi(self, B_widget):
        _translate = QtCore.QCoreApplication.translate
        B_widget.setWindowTitle(_translate("B_widget", "Form"))
        self.label.setText(_translate("B_widget", "B"))
        self.label_2.setText(_translate("B_widget", "STATUS:"))
        self.pushButton.setText(_translate("B_widget", "ENGAGE"))

from .AB_widget import AB_widget

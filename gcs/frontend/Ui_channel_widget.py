# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_channel_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_channel_widget(object):
    def setupUi(self, channel_widget):
        channel_widget.setObjectName("channel_widget")
        channel_widget.resize(220, 220)
        channel_widget.setMinimumSize(QtCore.QSize(220, 220))
        channel_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(channel_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(channel_widget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_supply = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_supply.setReadOnly(True)
        self.lineEdit_supply.setObjectName("lineEdit_supply")
        self.gridLayout.addWidget(self.lineEdit_supply, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_valve = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_valve.setReadOnly(True)
        self.lineEdit_valve.setObjectName("lineEdit_valve")
        self.gridLayout.addWidget(self.lineEdit_valve, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_current = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_current.setReadOnly(True)
        self.lineEdit_current.setObjectName("lineEdit_current")
        self.gridLayout.addWidget(self.lineEdit_current, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_cont = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cont.setReadOnly(True)
        self.lineEdit_cont.setObjectName("lineEdit_cont")
        self.gridLayout.addWidget(self.lineEdit_cont, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_status = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_status.setReadOnly(True)
        self.lineEdit_status.setObjectName("lineEdit_status")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_status)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_on = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_on.setFont(font)
        self.pushButton_on.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButton_on.setObjectName("pushButton_on")
        self.horizontalLayout.addWidget(self.pushButton_on)
        self.pushButton_on_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_on_2.setFont(font)
        self.pushButton_on_2.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_on_2.setObjectName("pushButton_on_2")
        self.horizontalLayout.addWidget(self.pushButton_on_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(channel_widget)
        QtCore.QMetaObject.connectSlotsByName(channel_widget)

    def retranslateUi(self, channel_widget):
        _translate = QtCore.QCoreApplication.translate
        channel_widget.setWindowTitle(_translate("channel_widget", "Form"))
        self.label_4.setText(_translate("channel_widget", "Supply"))
        self.label_5.setText(_translate("channel_widget", "V"))
        self.label_7.setText(_translate("channel_widget", "Valve"))
        self.label_8.setText(_translate("channel_widget", "V"))
        self.label_10.setText(_translate("channel_widget", "Current"))
        self.label_14.setText(_translate("channel_widget", "mA"))
        self.label_2.setText(_translate("channel_widget", "Cont"))
        self.label_6.setText(_translate("channel_widget", "STATUS:"))
        self.pushButton_on.setText(_translate("channel_widget", "On"))
        self.pushButton_on_2.setText(_translate("channel_widget", "Off"))


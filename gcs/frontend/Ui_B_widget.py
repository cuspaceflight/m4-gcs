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
        B_widget.resize(1700, 322)
        B_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(B_widget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(B_widget)
        self.frame_2.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_state = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_state.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_state.setFont(font)
        self.lineEdit_state.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_state.setReadOnly(True)
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.gridLayout.addWidget(self.lineEdit_state, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_mcu_temp = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mcu_temp.setFont(font)
        self.lineEdit_mcu_temp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_mcu_temp.setReadOnly(True)
        self.lineEdit_mcu_temp.setObjectName("lineEdit_mcu_temp")
        self.gridLayout.addWidget(self.lineEdit_mcu_temp, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_psu_v = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_psu_v.setFont(font)
        self.lineEdit_psu_v.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_psu_v.setReadOnly(True)
        self.lineEdit_psu_v.setObjectName("lineEdit_psu_v")
        self.gridLayout.addWidget(self.lineEdit_psu_v, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_firing_v = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_firing_v.setFont(font)
        self.lineEdit_firing_v.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_firing_v.setReadOnly(True)
        self.lineEdit_firing_v.setObjectName("lineEdit_firing_v")
        self.gridLayout.addWidget(self.lineEdit_firing_v, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_firing_i = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_firing_i.setFont(font)
        self.lineEdit_firing_i.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_firing_i.setReadOnly(True)
        self.lineEdit_firing_i.setObjectName("lineEdit_firing_i")
        self.gridLayout.addWidget(self.lineEdit_firing_i, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonArm = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonArm.setFont(font)
        self.pushButtonArm.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.pushButtonArm.setObjectName("pushButtonArm")
        self.horizontalLayout.addWidget(self.pushButtonArm)
        self.pushButtonDisarm = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDisarm.setFont(font)
        self.pushButtonDisarm.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(239, 41, 41);")
        self.pushButtonDisarm.setObjectName("pushButtonDisarm")
        self.horizontalLayout.addWidget(self.pushButtonDisarm)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.widget_chan = AB_widget(self.frame_2)
        self.widget_chan.setMinimumSize(QtCore.QSize(1180, 270))
        self.widget_chan.setObjectName("widget_chan")
        self.horizontalLayout_2.addWidget(self.widget_chan)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(B_widget)
        QtCore.QMetaObject.connectSlotsByName(B_widget)

    def retranslateUi(self, B_widget):
        _translate = QtCore.QCoreApplication.translate
        B_widget.setWindowTitle(_translate("B_widget", "Form"))
        self.label.setText(_translate("B_widget", "B"))
        self.label_5.setText(_translate("B_widget", "State:"))
        self.label_4.setText(_translate("B_widget", "MCU Temp:"))
        self.label_7.setText(_translate("B_widget", "°C"))
        self.label_3.setText(_translate("B_widget", "PSU Voltage:"))
        self.label_10.setText(_translate("B_widget", "V"))
        self.label_2.setText(_translate("B_widget", "Firing Voltage:"))
        self.label_8.setText(_translate("B_widget", "V"))
        self.label_6.setText(_translate("B_widget", "Firing Current:"))
        self.label_9.setText(_translate("B_widget", "mA"))
        self.pushButtonArm.setText(_translate("B_widget", "ARM"))
        self.pushButtonDisarm.setText(_translate("B_widget", "DISARM"))

from .AB_widget import AB_widget

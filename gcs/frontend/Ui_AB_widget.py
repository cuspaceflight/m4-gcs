# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Ui_AB_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AB_widget(object):
    def setupUi(self, AB_widget):
        AB_widget.setObjectName("AB_widget")
        AB_widget.resize(1651, 326)
        self.widget_6 = QtWidgets.QWidget(AB_widget)
        self.widget_6.setGeometry(QtCore.QRect(-10, -10, 1591, 311))
        self.widget_6.setObjectName("widget_6")
        self.frame = QtWidgets.QFrame(self.widget_6)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1571, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(241, 11, 1281, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = channel_1(self.layoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = channel_2(self.layoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = channel_3(self.layoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = channel_4(self.layoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = channel_5(self.layoutWidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 170, 219, 99))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.AB_status = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AB_status.setFont(font)
        self.AB_status.setReadOnly(True)
        self.AB_status.setObjectName("AB_status")
        self.gridLayout.addWidget(self.AB_status, 0, 1, 1, 1)

        self.retranslateUi(AB_widget)
        QtCore.QMetaObject.connectSlotsByName(AB_widget)

    def retranslateUi(self, AB_widget):
        _translate = QtCore.QCoreApplication.translate
        AB_widget.setWindowTitle(_translate("AB_widget", "Form"))
        self.pushButton.setText(_translate("AB_widget", "ENGAGE"))
        self.label.setText(_translate("AB_widget", "STATUS:"))

from .channel_1 import channel_1
from .channel_2 import channel_2
from .channel_3 import channel_3
from .channel_4 import channel_4
from .channel_5 import channel_5

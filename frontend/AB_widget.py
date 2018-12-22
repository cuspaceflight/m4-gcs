# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AB_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AB_widget(object):
    def setupUi(self, AB_widget):
        AB_widget.setObjectName("AB_widget")
        AB_widget.resize(1260, 300)
        self.widget_6 = QtWidgets.QWidget(AB_widget)
        self.widget_6.setGeometry(QtCore.QRect(10, 10, 1241, 281))
        self.widget_6.setObjectName("widget_6")
        self.frame = QtWidgets.QFrame(self.widget_6)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1221, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 1201, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = channel_widget(self.layoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = channel_widget(self.layoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = channel_widget(self.layoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = channel_widget(self.layoutWidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = channel_widget(self.layoutWidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)

        self.retranslateUi(AB_widget)
        QtCore.QMetaObject.connectSlotsByName(AB_widget)

    def retranslateUi(self, AB_widget):
        _translate = QtCore.QCoreApplication.translate
        AB_widget.setWindowTitle(_translate("AB_widget", "Form"))
        self.label_2.setText(_translate("AB_widget", "A/B"))
        self.pushButton_2.setText(_translate("AB_widget", "Button"))

from channel_widget import channel_widget

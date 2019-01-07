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
        self.widget = channel_1(AB_widget)
        self.widget.setMinimumSize(QtCore.QSize(234, 267))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignVCenter)
        self.widget_2 = channel_2(AB_widget)
        self.widget_2.setMinimumSize(QtCore.QSize(234, 267))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignVCenter)
        self.widget_3 = channel_3(AB_widget)
        self.widget_3.setMinimumSize(QtCore.QSize(234, 267))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignVCenter)
        self.widget_4 = channel_4(AB_widget)
        self.widget_4.setMinimumSize(QtCore.QSize(234, 267))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignVCenter)
        self.widget_5 = channel_5(AB_widget)
        self.widget_5.setMinimumSize(QtCore.QSize(234, 267))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5, 0, QtCore.Qt.AlignVCenter)

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

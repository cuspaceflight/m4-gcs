from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_widget import Ui_channel_widget

class channel_widget(QtWidgets.QWidget, Ui_channel_widget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

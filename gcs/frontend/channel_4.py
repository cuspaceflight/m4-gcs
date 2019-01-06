from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_4 import Ui_channel_4

class channel_4(QtWidgets.QWidget, Ui_channel_4):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

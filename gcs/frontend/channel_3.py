from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_3 import Ui_channel_3

class channel_3(QtWidgets.QWidget, Ui_channel_3):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

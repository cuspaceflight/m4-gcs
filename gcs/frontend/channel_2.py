from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_2 import Ui_channel_2

class channel_2(QtWidgets.QWidget, Ui_channel_2):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

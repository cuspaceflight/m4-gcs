from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_5 import Ui_channel_5

class channel_5(QtWidgets.QWidget, Ui_channel_5):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_channel_1 import Ui_channel_1

class channel_1(QtWidgets.QWidget, Ui_channel_1):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

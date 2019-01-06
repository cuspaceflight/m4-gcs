from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_B_widget import Ui_B_widget

class B_widget(QtWidgets.QWidget, Ui_B_widget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

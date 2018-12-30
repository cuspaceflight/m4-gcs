from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_A_widget import Ui_A_widget

class A_widget(QtWidgets.QWidget, Ui_A_widget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

from PyQt5 import QtCore, QtGui, QtWidgets
from .Ui_AB_widget import Ui_AB_widget

class AB_widget(QtWidgets.QWidget, Ui_AB_widget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

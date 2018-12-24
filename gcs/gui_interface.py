"""
GUI process
CUSF 2018/19
"""
from .packets import *
import time
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from multiprocessing import Pipe, Process
#from .frontend import *
from .frontend.main_window_real import Ui_MainWindow
#from .packets import *
import sys
import os
from timeit import default_timer as timer
from math import floor

script_dir = os.path.dirname(__file__)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainThd(QThread):
    new_pckt_sig = pyqtSignal(Packet)
    def __init__(self, window_pipe, usb_pipe):
        QThread.__init__(self)
        self.window_pipe = window_pipe
        self.usb_pipe = usb_pipe

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            if self.usb_pipe.poll(0.01):
                new_packet_usb = self.usb_pipe.recv()
                #self.emit(SIGNAL('new_packet(PyQt_PyObject)'),new_packet_usb)
                self.new_pckt_sig.emit(new_packet_usb)

            if self.window_pipe.poll(0.01):
                new_packet_window = self.window_pipe.recv()

                if isinstance(new_packet_window,Usb_command):
                    self.usb_pipe.send(new_packet_window)


class gcs_main_window(QMainWindow, Ui_MainWindow):
    """Inherit main window generated in QT5 Creator"""
    def __init__(self, usb_pipe, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        # Add slots and signals manually

        # Start update thread
        thread_end,self.gui_end = Pipe(duplex=False)  # So that QThread and gui don't use same pipe end at same time
        self.update_thread = MainThd(thread_end, usb_pipe)
        #self.connect(self.update_thread, SIGNAL("new_packet(PyQt_PyObject)"),self.new_packet)
        self.update_thread.new_pckt_sig.connect(self.new_packet)
        self.update_thread.start(QThread.LowPriority)

    def new_packet(self, packet):
        #TODO: handle new packet
        pass


# TODO:
#     - PyQt 5 GUI frontend runs in this process
#     - Once this works, can look into other technologies e.g. React JS


def run(usb_pipe, gui_exit):
    """Main loop

    usb_pipe -- pipe to/from USB process
    gui_exit -- gui exit signal"""

    app = QApplication(sys.argv)
    main_window = gcs_main_window(usb_pipe)
    main_window.show()
    app.exec_()
    gui_exit.set()  # This goes last, signals other processes to end

"""
GUI process
CUSF 2018/19
"""
from .packets import *
import time
import queue
import threading
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from multiprocessing import Pipe, Process
#from .frontend import *
from .frontend.main_window_real import Ui_MainWindow
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

    def __init__(self, window_in_q, usb_in_q, usb_out_q):
        QThread.__init__(self)
        self.window_in_q = window_in_q
        self.usb_in_q = usb_in_q
        self.usb_out_q = usb_out_q

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            try:
                new_packet_usb = self.usb_in_q.get(timeout=0.01)
                self.new_pckt_sig.emit(new_packet_usb)
            except queue.Empty:
                pass

            try:
                new_packet_window = self.window_in_q.get(timeout=0.01)
                if isinstance(new_packet_window, UsbCommand):
                    self.usb_out_q.put(new_packet_window)
            except queue.Empty:
                pass


class GcsMainWindow(QMainWindow, Ui_MainWindow):
    """Inherit main window generated in QT5 Creator"""
    def __init__(self, usb_in_q, usb_out_q, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        # Manual configuration
        diagram = QtGui.QPixmap('PID.png')
        diagram = diagram.scaledToWidth(1226)
        self.label_background.setPixmap(diagram)
        #self.widget_PID.setStyleSheet("image: url(./PID.png); background-attachment: fixed")

        # Add slots and signals manually

        # Start update thread
        window_out_q = queue.Queue()  # For communication between gui and QThread
        self.update_thread = MainThd(window_out_q, usb_in_q, usb_out_q)
        self.update_thread.new_pckt_sig.connect(self.new_packet)
        self.update_thread.start(QThread.LowPriority)

    def new_packet(self, packet):
        #TODO: handle new packet
        pass


# TODO:
#     - PyQt 5 GUI frontend runs in this process
#     - Once this works, can look into other technologies e.g. React JS


def produce(usb_pipe, gui_exit, out_q, in_q):
    while not gui_exit.is_set():
        # Receive from USB process
        if not out_q.full():
            if usb_pipe.poll(0.1):
                new_packet = usb_pipe.recv()
                out_q.put(new_packet)

        # Transmit to USB process
        try:
            new_cmd_packet = in_q.get(block=False)
            usb_pipe.send(new_cmd_packet)
        except queue.Empty:
            pass


def run(usb_pipe, gui_exit):
    """Main loop

    usb_pipe -- pipe to/from USB process
    gui_exit -- gui exit signal"""

    in_q = queue.Queue()   # Data from producer
    out_q = queue.Queue()  # Data to producer
    producer = threading.Thread(target=produce, args=(usb_pipe, gui_exit, in_q, out_q))
    producer.start()

    # # For debugging: ######################################################
    #
    # time.sleep(1)
    # for i in range(0, 20*200):
    #     cmd = BankStateCmdPacket(Bank.BANK_A.value, BankState.SAFE.value)
    #     usb_pipe.send(cmd)
    #     time.sleep(0.005)
    #     #print("{}\n".format(i))
    #
    # # cmd = ValveStateCmdPacket(Valve.A_CH1.value, ValveState.OFF.value)
    # # usb_pipe.send(cmd)
    # # time.sleep(1)
    # #
    # # cmd = ConfigCmdPacket(Valve.A_CH1.value, Valve.A_CH2.value, Valve.B_CH4.value, Valve.B_CH5.value, Valve.A_CH5.value)
    # # usb_pipe.send(cmd)
    # print("\nDone sending\n")
    # time.sleep(60)
    # # End debugging: ######################################################

    app = QApplication(sys.argv)
    main_window = GcsMainWindow(in_q, out_q)
    main_window.show()
    app.exec_()

    gui_exit.set()  # Signals other processes to end when window is closed
    producer.join()


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

    def __init__(self, usb_pipe, gui_exit, in_q):
        QThread.__init__(self)
        self.usb_pipe = usb_pipe
        self.gui_exit = gui_exit
        self.in_q = in_q

    def __del__(self):
        self.wait()

    def run(self):
        while not self.gui_exit.is_set():
            # Receive from USB process
            if self.usb_pipe.poll(0.1):
                new_packet_usb = self.usb_pipe.recv()
                self.new_pckt_sig.emit(new_packet_usb)

            # Transmit to USB process
            try:
                new_cmd_packet = self.in_q.get(block=False)
                self.usb_pipe.send(new_cmd_packet)
            except queue.Empty:
                pass

            # try:
            #     new_packet_window = self.window_in_q.get(timeout=0.01)
            #     if isinstance(new_packet_window, UsbCommand):
            #         self.usb_out_q.put(new_packet_window)
            # except queue.Empty:
            #     pass


class GcsMainWindow(QMainWindow, Ui_MainWindow):
    """Inherit main window generated in QT5 Creator"""
    def __init__(self, usb_pipe, gui_exit, window_to_thread_q, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        self.usb_out_q = window_to_thread_q

        ##
        # Manual configuration
        ##

        # Plumbing diagram as background image
        diagram = QtGui.QPixmap('PID.png')
        diagram = diagram.scaledToWidth(1226)
        self.label_background.setPixmap(diagram)

        # Fill in channel descriptions
        # TODO: parse from yaml file
        self.widget_A.widget_chan.chan1.label_description.setText("NOS Bottle 1")
        self.widget_A.widget_chan.chan2.label_description.setText("Fill Line Vent")
        self.widget_A.widget_chan.chan3.label_description.setText("NOS Bottle 2")
        self.widget_A.widget_chan.chan4.label_description.setText("Flight Tank Vent")
        self.widget_A.widget_chan.chan5.label_description.setText("Flight Tank Isolation")
        self.widget_B.widget_chan.chan1.label_description.setText("Air Supply")
        self.widget_B.widget_chan.chan2.label_description.setText("Propane Supply")
        self.widget_B.widget_chan.chan3.label_description.setText("Ignitor")
        self.widget_B.widget_chan.chan4.label_description.setText("[Unused]")
        self.widget_B.widget_chan.chan5.label_description.setText("[Unused]")

        ##
        # Add slots and signals manually:
        ##

        # Arming buttons
        self.widget_A.pushButtonArm.clicked.connect(lambda: self.arm_bank(Bank.BANK_A.value, BankState.ARMED.value))
        self.widget_A.pushButtonDisarm.clicked.connect(lambda: self.arm_bank(Bank.BANK_A.value, BankState.SAFE.value))
        self.widget_B.pushButtonArm.clicked.connect(lambda: self.arm_bank(Bank.BANK_B.value, BankState.ARMED.value))
        self.widget_B.pushButtonDisarm.clicked.connect(lambda: self.arm_bank(Bank.BANK_B.value, BankState.SAFE.value))

        # Channel A firing buttons
        self.widget_A.widget_chan.chan1.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH1.value, ValveState.ON.value))
        self.widget_A.widget_chan.chan1.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH1.value, ValveState.OFF.value))
        self.widget_A.widget_chan.chan2.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH2.value, ValveState.ON.value))
        self.widget_A.widget_chan.chan2.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH2.value, ValveState.OFF.value))
        self.widget_A.widget_chan.chan3.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH3.value, ValveState.ON.value))
        self.widget_A.widget_chan.chan3.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH3.value, ValveState.OFF.value))
        self.widget_A.widget_chan.chan4.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH4.value, ValveState.ON.value))
        self.widget_A.widget_chan.chan4.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH4.value, ValveState.OFF.value))
        self.widget_A.widget_chan.chan5.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH5.value, ValveState.ON.value))
        self.widget_A.widget_chan.chan5.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH5.value, ValveState.OFF.value))

        # Channel B firing buttons
        self.widget_B.widget_chan.chan1.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH1.value, ValveState.ON.value))
        self.widget_B.widget_chan.chan1.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH1.value, ValveState.OFF.value))
        self.widget_B.widget_chan.chan2.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH2.value, ValveState.ON.value))
        self.widget_B.widget_chan.chan2.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH2.value, ValveState.OFF.value))
        self.widget_B.widget_chan.chan3.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH3.value, ValveState.ON.value))
        self.widget_B.widget_chan.chan3.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH3.value, ValveState.OFF.value))
        self.widget_B.widget_chan.chan4.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH4.value, ValveState.ON.value))
        self.widget_B.widget_chan.chan4.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH4.value, ValveState.OFF.value))
        self.widget_B.widget_chan.chan5.fields.pushButton_on.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH5.value, ValveState.ON.value))
        self.widget_B.widget_chan.chan5.fields.pushButton_off.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH5.value, ValveState.OFF.value))

        # TODO: configure from yaml file
        # Closed
        self.pushButton_VC1.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH1.value, ValveState.OFF.value))
        self.pushButton_VC2.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH2.value, ValveState.OFF.value))
        self.pushButton_VC3.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH3.value, ValveState.OFF.value))
        self.pushButton_VC4.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH4.value, ValveState.OFF.value))
        self.pushButton_VC6.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH5.value, ValveState.OFF.value))

        self.pushButton_VC9.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH1.value, ValveState.OFF.value))
        self.pushButton_VC13.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH2.value, ValveState.OFF.value))

        # Open
        self.pushButton_VO1.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH1.value, ValveState.ON.value))
        self.pushButton_VO2.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH2.value, ValveState.ON.value))
        self.pushButton_VO3.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH3.value, ValveState.ON.value))
        self.pushButton_VO4.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH4.value, ValveState.ON.value))
        self.pushButton_VO6.clicked.connect(
            lambda: self.fire_valve(Valve.A_CH5.value, ValveState.ON.value))

        self.pushButton_VO9.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH1.value, ValveState.ON.value))
        self.pushButton_VO13.clicked.connect(
            lambda: self.fire_valve(Valve.B_CH2.value, ValveState.ON.value))

        self.pushButtonUsbConnect.clicked.connect(lambda: self.toggle_con(self.pushButtonUsbConnect))

        self.packet_timer_counter = 0
        self.packet_timer = QTimer()
        self.packet_timer.timeout.connect(self.timer_cb)
        self.packet_timer.start(100)  # ms

        # Start update thread
        self.update_thread = MainThd(usb_pipe, gui_exit, window_to_thread_q)
        self.update_thread.new_pckt_sig.connect(self.new_packet)
        self.update_thread.start(QThread.LowPriority)

    def timer_cb(self):
        self.packet_timer_counter += 1
        self.lineEdit_timer.setText("{}".format(self.packet_timer_counter/10))
        self.lineEdit_timer.setCursorPosition(0)

    def fire_valve(self, valve, value):
        packet = ValveStateCmdPacket(valve, value)
        self.send_out(packet)

    def arm_bank(self, bank, bankstate):
        packet = BankStateCmdPacket(bank, bankstate)
        self.send_out(packet)

    def toggle_con(self, button):
        if button.isChecked():
            # Connect
            button.setText("USB Disconnect")
            self.send_out(UsbCommand(True))
        else:
            # Disconnect
            button.setText("USB Connect")
            self.send_out(UsbCommand(False))

    def new_packet(self, packet):
        """Handle new packet"""

        # First reset the counter
        self.packet_timer_counter = 0
        self.lineEdit_timer.setText("{}".format(self.packet_timer_counter))
        self.lineEdit_timer.setCursorPosition(0)

        packet.printout(self.textEdit_printout)
        if not packet.valid:
            return  # Print in terminal but don't display
        if isinstance(packet, ChannelStatusPacket):
            self.handle_channel_status_packet(packet)
        elif isinstance(packet, BankStatusPacket):
            self.handle_bank_status_packet(packet)

    def handle_channel_status_packet(self, packet):
        if packet.bank == Bank.BANK_A.value:
            wdgt = self.widget_A
            # TODO: configure from yaml file
            labels = [self.label_V1,
                      self.label_V2,
                      self.label_V3,
                      self.label_V4,
                      self.label_V6,
                      self.label_V9,
                      self.label_V13]
        elif packet.bank == Bank.BANK_B.value:
            wdgt = self.widget_B
            # TODO: configure from yaml file
            labels = [self.label_V9, self.label_V13]
        else:
            # Invalid packet
            return

        channels = [wdgt.widget_chan.chan1,
                    wdgt.widget_chan.chan2,
                    wdgt.widget_chan.chan3,
                    wdgt.widget_chan.chan4,
                    wdgt.widget_chan.chan5]

        for i in range(0, 5):
            s = packet.channel_status[i]
            channels[i].fields.lineEdit_supply.setText("{}".format(s.firing_v))
            channels[i].fields.lineEdit_valve.setText("{}".format(s.output_v))
            channels[i].fields.lineEdit_current.setText("{}".format(s.output_c))
            channels[i].fields.lineEdit_cont.setText(Continuity.to_string(s.continuity))
            channels[i].fields.lineEdit_status.setText(ValveState.to_string(s.state))

            channels[i].fields.lineEdit_supply.setCursorPosition(0)
            channels[i].fields.lineEdit_valve.setCursorPosition(0)
            channels[i].fields.lineEdit_current.setCursorPosition(0)
            channels[i].fields.lineEdit_cont.setCursorPosition(0)
            channels[i].fields.lineEdit_status.setCursorPosition(0)

            if s.state == ValveState.OFF.value:
                labels[i].setText("CLOSED")
                labels[i].setStyleSheet('background-color: rgb(239, 41, 41); color: rgb(255, 255, 255);')
            elif s.state == ValveState.ON.value:
                labels[i].setText("OPEN")
                labels[i].setStyleSheet('background-color: rgb(138, 226, 52); color: rgb(0, 0, 0);')

    def handle_bank_status_packet(self, packet):
        if packet.bank == Bank.BANK_A.value:
            wdgt = self.widget_A
        elif packet.bank == Bank.BANK_B.value:
            wdgt = self.widget_B
        else:
            # Invalid packet
            return

        wdgt.lineEdit_state.setText(BankState.to_string(packet.state))
        wdgt.lineEdit_mcu_temp.setText("{}".format(packet.mcu_temp))
        wdgt.lineEdit_psu_v.setText("{}".format(packet.psu_v))
        wdgt.lineEdit_firing_v.setText("{}".format(packet.firing_v))
        wdgt.lineEdit_firing_i.setText("{}".format(packet.firing_c))

        wdgt.lineEdit_state.setCursorPosition(0)
        wdgt.lineEdit_mcu_temp.setCursorPosition(0)
        wdgt.lineEdit_psu_v.setCursorPosition(0)
        wdgt.lineEdit_firing_v.setCursorPosition(0)
        wdgt.lineEdit_firing_i.setCursorPosition(0)

    def send_out(self, packet):
        # Send a packet to the USB process
        packet.printout(self.textEdit_printout)
        self.usb_out_q.put(packet)


# TODO:
#     - PyQt 5 GUI frontend runs in this process
#     - Once this works, can look into other technologies e.g. React JS


# def produce(usb_pipe, gui_exit, out_q, in_q):
#     while not gui_exit.is_set():
#         # Receive from USB process
#         if not out_q.full():
#             if usb_pipe.poll(0.1):
#                 new_packet = usb_pipe.recv()
#                 out_q.put(new_packet)
#
#         # Transmit to USB process
#         try:
#             new_cmd_packet = in_q.get(block=False)
#             usb_pipe.send(new_cmd_packet)
#         except queue.Empty:
#             pass


def run(usb_pipe, gui_exit):
    """Main loop

    usb_pipe -- pipe to/from USB process
    gui_exit -- gui exit signal"""

    window_to_thread_q = queue.Queue()
    # producer = threading.Thread(target=produce, args=(usb_pipe, gui_exit, in_q, out_q))
    # producer.start()

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
    main_window = GcsMainWindow(usb_pipe, gui_exit, window_to_thread_q)
    main_window.show()
    app.exec_()

    gui_exit.set()  # Signals other processes to end when window is closed


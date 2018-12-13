"""
USB data handling process
CUSF 2018/19
"""

import serial
import time
from .packets import *

# TODO:
#     - Handle incoming and outgoing USB data


def run(port, gui_pipe, log_pipe, gui_exit):
    """Main USB process function

    port     -- serial port to use
    gui_pipe -- pipe to/from GUI process
    log_pipe -- pipe to/from logging process
    gui_exit -- gui exit signal
        """

    # initialise serial port
    ser = serial.Serial(port=port, write_timeout=0, timeout=0.05)  # Open serial port
    time.sleep(3)

    # continuously poll port for packets
    while not gui_exit.is_set():
        # Main loop

        # Send over USB
        if gui_pipe.poll():
            # Receive incoming commands from the gui process
            cmd = gui_pipe.recv()
            # need to define Usb_command in gui code:command sent from gui.

            # TODO: define internal packets
            if isinstance(cmd, UsbCommand):
                if cmd.conn and not ser.is_open:
                    # Connect
                    ser.open()
                elif not cmd.conn and ser.is_open:
                    # Disconnect
                    ser.close()
            elif isinstance(cmd, CmdPacket):
                if ser.is_open:
                    ser.write(cmd.packed_bytes)

        # Receive over USB
        # TODO: check whether first byte is within the list of valid packet IDs before receiving the next 127 bytes
        if ser.is_open:
            if ser.in_waiting > 4094:
                print("USB buffer full!")
            elif ser.in_waiting >= 128:
                serial_buffer = ser.read(128)
                message = Packet(serial_buffer)

            if gui_exit.is_set():
                break  # End process
            else:
                log_pipe.send(message)

        else:
            time.sleep(0.1)





"""
USB data handling process
CUSF 2018/19
"""

import serial
from .packets import *

DEBUG = False
START_BYTE = 0x7E
# Escape all 0x7E and 0x7D to 0x7D 0x5E and 0x7D 0x5D
ESCAPE_BYTE = 0x7D
ESCAPE_BYTE_START = 0x5E
ESCAPE_BYTE_ESC = 0x5D

MIN_PACKET_SIZE = 1+RX_PCKT_SIZE  # Start byte + min size

# TODO:
#     - Handle incoming and outgoing USB data


def serial_write(b, ser):
    """Add start bit and escape substitutions before transmitting bytes over USB

    b   -- bytes to be modified before transmission
    ser -- pyserial Serial object"""
    tx_buf = bytearray([START_BYTE]) + bytearray(b)
    for i in range(1, len(tx_buf)):
        if tx_buf[i] == bytearray([START_BYTE]):
            tx_buf[i:i+1] = bytearray([ESCAPE_BYTE, ESCAPE_BYTE_START])
        elif tx_buf[i] == bytearray([ESCAPE_BYTE]):
            tx_buf[i:i+1] = bytearray([ESCAPE_BYTE, ESCAPE_BYTE_ESC])

    ser.write(tx_buf)


def serial_read(ser, serial_buffer):
    """Handle escape substitutions before passing bytes to packet constructors

    ser           -- pyserial Serial object
    serial_buffer -- bytearray to store received bytes"""
    counter = 0
    escape = False
    rx_byte = bytearray()
    while counter < RX_PCKT_SIZE:
        rx_byte = ser.read()
        if len(rx_byte) == 0:
            # Timeout
            break
        else:
            if rx_byte == bytearray([ESCAPE_BYTE]):
                escape = True
                continue
            else:
                if escape:
                    if rx_byte == bytearray([ESCAPE_BYTE_START]):
                        rx_byte = bytearray([START_BYTE])
                    elif rx_byte == bytearray([ESCAPE_BYTE_ESC]):
                        rx_byte = bytearray([ESCAPE_BYTE])
                    escape = False

                serial_buffer += rx_byte
                counter += 1

    if len(rx_byte) == 0:
        # Error e.g.
        return 1
    else:
        return 0  # Success


def run(port, gui_pipe, log_pipe, gui_exit, usb_ready):
    """Main USB process function

    port     -- serial port to use
    gui_pipe -- pipe to/from GUI process
    log_pipe -- pipe to/from logging process
    gui_exit -- gui exit signal
        """

    # initialise serial port
    ser = serial.Serial(port=port, baudrate=115200, write_timeout=0, timeout=0.05)  # Open serial port

    # continuously poll port for packets
    while not gui_exit.is_set():
        # Main loop
        usb_ready.set()

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
                    # Transmit command over USB
                    serial_write(cmd.packed_bytes, ser)
                    log_pipe.send(cmd)
                    if DEBUG:
                        print_bytes = struct.unpack('<{}B'.format(len(cmd.packed_bytes)), cmd.packed_bytes)
                        print([hex(i) for i in print_bytes])
                        print("\n")

        # Receive over USB
        if ser.is_open:
            if ser.in_waiting > 4094:
                print("USB buffer full!")
            if ser.in_waiting > 0:
                # Assumes baudrate is high enough to prevent timeout
                rx_byte = 0
                while rx_byte != bytearray([START_BYTE]):
                    rx_byte = ser.read()
                    if len(rx_byte) == 0:
                        # Timeout
                        break
                if len(rx_byte) == 0:
                    # Timeout
                    break
                else:

                    serial_buffer = bytearray()
                    read_res = serial_read(ser, serial_buffer)

                    if read_res == 1:
                        # Timeout
                        break
                    else:
                        if int(serial_buffer[0]) == PcktTypes.CHANNEL_STATUS:
                            message = ChannelStatusPacket(serial_buffer)
                        elif int(serial_buffer[0]) == PcktTypes.BANK_STATUS:
                            message = BankStatusPacket(serial_buffer)
                        else:
                            message = Packet(serial_buffer)

                        if DEBUG:
                            message.print_to_terminal()

                        if gui_exit.is_set():
                            break  # End process
                        else:
                            log_pipe.send(message)
                            gui_pipe.send(message)

        else:
            time.sleep(0.1)





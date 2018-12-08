"""
USB data handling process
CUSF 2018/19
"""

import serial
import time

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

    serial_buffer = bytearray()

    # continuously poll port for packets
    while not gui_exit.is_set():
        # Main loop
        if gui_pipe.poll():
            # Receive incoming
            # commands from the gui process
            cmd = gui_pipe.recv()
            # need to define Usb_command in gui code:command sent from gui.
            if isinstance(cmd, Usb_command):
                if cmd.conn and not ser.is_open:
                    # Connect
                    ser.open()
                elif not cmd.conn and ser.is_open:
                    # Disconnect
                    ser.close()
                if ser.is_open:
                    ser.write(cmd.to_binary())
        if ser.is_open:
            if int(ser.in_waiting) > 4094:
                print("USB buffer full!")
            byte_in = ser.read()
            if not byte_in:
                # Timeout, clear buffer and continue while loop
                serial_buffer = bytearray()
                continue
            else:
                serial_buffer.extend(byte_in)
                message = Packet.construct(serial_buffer[0:128])

            if gui_exit.is_set():
                break  # End process
            else:
                log_pipe.send(message)

            #clear buffer
            serial_buffer = bytearray()

        else:
            time.sleep(0.1)





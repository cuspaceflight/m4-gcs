"""
Martlet 4/Pulsar Ground Control Software
CUSF 2018/19
"""
from gcs import usb
from gcs import gui_interface
from gcs import logging
import time
import signal
import multiprocessing
import argparse

# Todo: freeze script into executable once done

def run(args):
    """Initialise and run the backend.

    args -- command line arguments
    """
    ############################################################################
    # Create communication links between processes:
    ############################################################################
    print("Initialising Martlet IV Ground Station...")

    # Pipe USB data to logging processes
    log_usb_pipe, usb_log_pipe = multiprocessing.Pipe(duplex=False)

    # Duplex pipe between usb and gui processes
    usb_gui_pipe, gui_usb_pipe = multiprocessing.Pipe(True)

    ############################################################################
    # Define and start processes
    ############################################################################
    gui_exit = multiprocessing.Event()  # Flag for gui exit
    gui_exit.clear()

    print("Starting processes...")
    # Start gui/main process
    gui_process = multiprocessing.Process(target=gui_interface.run, args=(gui_usb_pipe, gui_exit))
    gui_process.start()

    # Start logging process
    log_process = multiprocessing.Process(target=logging.run, args=(log_usb_pipe, gui_exit, "../logs"))
    log_process.start()

    # Start usb parsing process
    usb_process = multiprocessing.Process(target=usb.run, args=(args.port, usb_gui_pipe, usb_log_pipe, gui_exit))
    usb_process.start()

    print("Running...")
    gui_process.join()
    print("Exiting...")
    print("GUI process ended")
    usb_process.join()
    print("USB process ended")
    log_process.join()
    print("Logging process ended")
    time.sleep(0.2)


signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on Ctrl-C

# Process arguments
parser = argparse.ArgumentParser(description=
                                 """Martlet IV Ground Control Software.
                                 Connect to Firing Controller on given serial port (default /dev/ttyACM0)""")
parser.add_argument('--port', dest='port', type=str, nargs='?',
                    default='/dev/ttyACM0', help='Serial port to use')

run(parser.parse_args())



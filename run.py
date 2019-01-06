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
    log_ready = multiprocessing.Event()  # Log process ready flag
    log_ready.clear()

    usb_ready = multiprocessing.Event()  # USB process ready flag
    usb_ready.clear()

    gui_exit = multiprocessing.Event()  # Flag for gui exit
    gui_exit.clear()

    print("Starting processes...")
    # Todo: add ready signal to each process?

    # Start gui/main process
    gui_process = multiprocessing.Process(target=gui_interface.run, args=(gui_usb_pipe, gui_exit))
    gui_process.start()

    # Start logging process
    log_process = multiprocessing.Process(target=logging.run, args=(log_usb_pipe, gui_exit, log_ready, "../logs"))
    log_process.start()

    while not log_ready.is_set():
        # Wait for logging process to finish starting up
        time.sleep(0.1)

    # Start usb parsing process
    usb_process = multiprocessing.Process(target=usb.run, args=(args.port, usb_gui_pipe, usb_log_pipe, gui_exit, usb_ready))
    usb_process.start()

    while not usb_ready.is_set():
        # Wait for USB process to finish starting up
        time.sleep(0.1)

    # # Start gui/main process
    # gui_process = multiprocessing.Process(target=gui_interface.run, args=(gui_usb_pipe, gui_exit))
    # gui_process.start()

    print("Running...")
    gui_process.join()
    print("Exiting...")
    print("GUI process ended")
    usb_process.join()
    print("USB process ended")
    log_process.join()
    print("Logging process ended")
    time.sleep(0.2)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Exit on Ctrl-C

    # Process arguments
    parser = argparse.ArgumentParser(description=
                                     """Martlet IV Ground Control Software.
                                     Connect to Firing Controller on given serial port (default '/dev/ttyACM0')""")
    parser.add_argument('-p', dest='port', type=str, nargs='?',
                        default='/dev/ttyACM0', help='Serial port to use')

    run(parser.parse_args())



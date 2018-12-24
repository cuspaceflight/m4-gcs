"""
GUI process
CUSF 2018/19
"""
from .packets import *
import time
import queue
import threading

# TODO:
#     - PyQt 5 GUI frontend runs in this process
#     - Once this works, can look into other technologies e.g. React JS


def produce(usb_pipe, gui_exit, q):
    while not gui_exit.is_set():
        if not q.full():
            if usb_pipe.poll(0.1):
                new_packet = usb_pipe.recv()
                q.put(new_packet)


def run(usb_pipe, gui_exit):
    """Main loop

    usb_pipe -- pipe to/from USB process
    gui_exit -- gui exit signal"""

    # For debugging: ######################################################

    time.sleep(1)
    for i in range(0, 20*200):
        cmd = BankStateCmdPacket(Bank.BANK_A.value, BankState.SAFE.value)
        usb_pipe.send(cmd)
        time.sleep(0.005)
        #print("{}\n".format(i))

    # cmd = ValveStateCmdPacket(Valve.A_CH1.value, ValveState.OFF.value)
    # usb_pipe.send(cmd)
    # time.sleep(1)
    #
    # cmd = ConfigCmdPacket(Valve.A_CH1.value, Valve.A_CH2.value, Valve.B_CH4.value, Valve.B_CH5.value, Valve.A_CH5.value)
    # usb_pipe.send(cmd)
    print("\nDone sending\n")
    time.sleep(60)
    # End debugging: ######################################################
    q = queue.Queue()
    producer = threading.Thread(target=produce, args=(usb_pipe, gui_exit, q))
    producer.start()

    #TODO: run gui here

    gui_exit.set()  # This goes last, signals other processes to end
    producer.join()


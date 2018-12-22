"""
GUI process
CUSF 2018/19
"""
from .packets import *
import time

# TODO:
#     - PyQt 5 GUI frontend runs in this process
#     - Once this works, can look into other technologies e.g. React JS


def run(usb_pipe, gui_exit):
    """Main loop

    usb_pipe -- pipe to/from USB process
    gui_exit -- gui exit signal"""

    # For debugging: ######################################################

    # Send 3 example packets then wait to receive some
    time.sleep(1)
    cmd = BankStateCmdPacket(Bank.BANK_A.value, BankState.SAFE.value)
    usb_pipe.send(cmd)
    time.sleep(1)

    cmd = ValveStateCmdPacket(Valve.A_CH1.value, ValveState.OFF.value)
    usb_pipe.send(cmd)
    time.sleep(1)

    cmd = ConfigCmdPacket(Valve.A_CH1.value, Valve.A_CH2.value, Valve.B_CH4.value, Valve.B_CH5.value, Valve.A_CH5.value)
    usb_pipe.send(cmd)
    time.sleep(30)
    # End debugging: ######################################################

    gui_exit.set()  # This goes last, signals other processes to end


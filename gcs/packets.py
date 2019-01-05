"""
USB packet definitions
CUSF 2018/19
"""

import json
import struct
import time
from enum import Enum
from PyQt5 import QtCore, QtGui


def fletcher32(bytes_arg):
    """Compute Fletcher-32 checksum
    Based on: azbshiri (https://gist.github.com/globby/9337839)

    bytes_arg -- bytes to perform checksum calculation on"""
    a = struct.unpack("<{}B".format(len(bytes_arg)), bytes_arg)
    b = [sum(a[:i]) % 65535 for i in range(len(a)+1)]
    return (sum(b) % 65535 << 16) | max(b)

# RX Packets ########################################################################
# Constants:
# TODO:check constants
RX_PCKT_SIZE = 128
PAYLOAD_START = 8
PAYLOAD_END = RX_PCKT_SIZE - 4
CHANNEL_STATUS_SIZE = 14


class PcktTypes(Enum):
    CMD             = 0
    CHANNEL_STATUS  = 1
    BANK_STATUS     = 2

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class Cmd(Enum):
    BANK_STATE = 0xF0
    VALVE_STATE = 0xF1
    #UPDATE_CONFIG = 0xF2

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class ValveState(Enum):
    ON = 0x10
    OFF = 0x1F

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class BankState(Enum):
    ENERGISED = 0x1A
    ARMED = 0x1D
    SAFE = 0x12
    ISOLATED = 0x16

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class Bank(Enum):
    BANK_A = 0xA0
    BANK_B = 0xB0

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class Valve(Enum):
    A_CH1 = 0xA1
    A_CH2 = 0xA2
    A_CH3 = 0xA3
    A_CH4 = 0xA4
    A_CH5 = 0xA5
    #MAIN_VALVE = 0xA6

    B_CH1 = 0xB1
    B_CH2 = 0xB2
    B_CH3 = 0xB3
    B_CH4 = 0xB4
    B_CH5 = 0xB5
    IGNITER = 0xB6

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


# TODO: define ack packets

# Current packet variables:       data_struct : Raw packet data (save just in case it's needed later)
#                                 packet_type : What data is contained in packet
#                                 timestamp   : When the data was received
#                                 checksum    : Received checksum
#                                 csum_calc   : Calculated checksum
# Input data structure: 128 bytes, of which the first 8 bytes are meta data.
# Meta data structure : Byte 0   : packet_type
#                       Byte 1-3 : RESERVED
#                       Byte 4-7 : timestamp
class Packet(object):
    """Base class"""
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""

        self.data_struct = input_struct

        meta_data = struct.unpack('<BBBBI', self.data_struct[0:PAYLOAD_START])

        self.type = meta_data[0]
        self.valid = PcktTypes.has_value(self.type)

        self.timestamp = meta_data[4]

        # Fletcher-32 checksum
        c_sum = struct.unpack('<I', self.data_struct[PAYLOAD_END:RX_PCKT_SIZE])
        self.checksum = c_sum[0]

        # Calculate checksum and ensure it matches self.checksum, store result in self.valid bool
        self.csum_calc = fletcher32(self.data_struct[:PAYLOAD_END])
        self.valid &= (self.csum_calc == self.checksum)

    def print_with(self, print_func):
        """Print packet using provided function

        print_func -- function to use to print"""
        print_func("## RX ##")
        print_func("ID:                  {}\n".format(self.type))
        print_func("Timestamp:           {}\n".format(self.timestamp))
        print_func("Received checksum:   {}\n".format(self.checksum))
        print_func("Calculated checksum: {}\n".format(self.checksum))
        print_func("Valid:               {}\n".format(self.checksum))

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        textbox.moveCursor(QtGui.QTextCursor.End)
        textbox.ensureCursorVisible()
        self.print_with(textbox.insertPlainText)
        textbox.insertPlainText("\n\n")

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""
        self.print_with(filename.write)
        filename.write("\n\n")

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        json.dump(self.__dict__, filename)

    def print_to_terminal(self):
        """Print to the terminal, useful for debugging"""
        self.print_with(print)
        print("\n\n")


class BankStatusPacket(Packet):
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        Packet.__init__(self, input_struct)

        payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]

        bank_status = struct.unpack('<BBffff', payload[0:18])
        # Todo: add comments with units for each
        self.bank = bank_status[0]
        self.valid &= Bank.has_value(self.bank)

        self.state = bank_status[1]
        self.valid &= BankState.has_value(self.state)

        self.mcu_temp = bank_status[2]
        self.psu_v = bank_status[3]
        self.firing_v = bank_status[4]
        self.firing_c = bank_status[5]

    def print_with(self, print_func):
        """Print with supplied function

        print_func -- print function to use"""
        Packet.print_with(print_func)
        print_func("Bank:                {}\n".format(self.bank))
        print_func("State:               {}\n".format(self.state))
        print_func("MCU Temp:            {}\n".format(self.mcu_temp))
        print_func("PSU Voltage:         {}\n".format(self.psu_v))
        print_func("Firing Voltage:      {}\n".format(self.firing_v))
        print_func("Firing Current:      {}\n".format(self.firing_c))


class ChannelStatus(object):
    """Not a packet, but a component of ChannelStatusPacket"""

    def __init__(self, input_struct=bytes(CHANNEL_STATUS_SIZE)):
        """Unpack incoming bytes

        input_struct -- incoming bytes to be unpacked"""
        channel_status = struct.unpack('<BfffB', input_struct)
        # Todo: add comments with units for each
        self.state = channel_status[0]
        self.firing_v = channel_status[1]
        self.output_v = channel_status[2]
        self.output_c = channel_status[3]
        self.continuity = channel_status[4]

    def print_with(self, print_func):
        print_func("Firing Voltage:      {}\n".format(self.firing_v))
        print_func("Output Voltage:      {}\n".format(self.output_v))
        print_func("Output Current:      {}\n".format(self.output_c))
        print_func("Continuity:          {}\n".format(self.continuity))

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print into"""
        self.print_with(textbox.insertPlainText)
        #textbox.insertPlainText("\n\n")

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""

        self.print_with(filename.write)
        #filename.write("\n\n")

    def print_to_terminal(self):
        """Print to the terminal, useful for debugging"""
        self.print_with(print)
        #print("\n\n")


class ChannelStatusPacket(Packet):
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        Packet.__init__(self, input_struct)

        payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]
        self.bank = struct.unpack('<B', payload[0])
        self.valid &= Bank.has_value(self.bank)
        self.channel_status = []
        for i in range(0, 5):
            self.channel_status.append(ChannelStatus(payload[i * CHANNEL_STATUS_SIZE:(i + 1) * CHANNEL_STATUS_SIZE]))

    def print_with(self, print_func):
        """Print with supplied function

        print_func -- print function to use"""
        Packet.print_with(print_func)
        print_func("Bank:                {}\n".format(self.bank))
        for i in range(0, 5):
            self.channel_status[i].print_with(print_func)


# Tx Packets ########################################################################


class CmdPacket(object):
    """Base PC to valve controller command packet"""
    def __init__(self, cmd):
        if not Cmd.has_value(cmd):
            raise ValueError("Invalid command ID")
        self.type = PcktTypes.CMD.value
        self.cmd = cmd
        self.timestamp = int(round(time.time()))
        self.packed_bytes = struct.pack('<B3xIB', self.type, self.timestamp, self.cmd)
        self.checksum = None
        self.num_padding = 115

    def pack_cmd(self):
        """Pack fields into byte form for transmission over USB"""
        self.packed_bytes += struct.pack('<{}x'.format(self.num_padding))  # Remaining payload
        self.checksum = fletcher32(self.packed_bytes)
        self.pack_checksum(self)

    def pack_checksum(self):
        """Calculate checksum using packed bytes & append it to the bytes"""
        # Calculate checksum and ensure it matches self.checksum, store result in self.valid bool
        self.checksum = fletcher32(self.packed_bytes)
        self.packed_bytes += struct.pack('<I', self.checksum)

    def print_with(self, print_func):
        print_func("## TX ##")
        print_func("ID:                  {}\n".format(self.type))
        print_func("Timestamp:           {}\n".format(self.timestamp))
        print_func("Command:             {}\n".format(self.cmd))
        print_func("Checksum:            {}\n".format(self.checksum))

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        textbox.moveCursor(QtGui.QTextCursor.End)
        textbox.ensureCursorVisible()
        self.print_with(textbox.insertPlainText)
        textbox.insertPlainText("\n\n")

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""
        self.print_with(filename.write)
        filename.write("\n\n")

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        json.dump(self.__dict__, filename)

    def print_to_terminal(self):
        """Print to the terminal, useful for debugging"""
        self.print_with(print)
        print("\n\n")


class BankStateCmdPacket(CmdPacket):
    """Command to set bank status"""
    def __init__(self, bank, state):
        CmdPacket.__init__(self, Cmd.BANK_STATE.value)

        if not Bank.has_value(bank):
            raise ValueError("Invalid bank ID")
        if not BankState.has_value(state):
            raise ValueError("Invalid bank state")

        self.bank = bank
        self.state = state
        self.num_padding -= 2

        self.pack_cmd(self)

    def pack_cmd(self):
        """Pack fields into byte form for transmission over USB"""
        self.packed_bytes += struct.pack('<BB', self.bank, self.state)
        self.packed_bytes += struct.pack('<{}x'.format(self.num_padding))  # Remaining payload
        self.pack_checksum(self)

    def print_with(self, print_func):
        CmdPacket.print_with(print_func)
        print_func("Bank:                {}\n".format(self.bank))
        print_func("State:               {}\n".format(self.state))


class ValveStateCmdPacket(CmdPacket):
    """Command to set channel/valve status"""
    def __init__(self, valve, state):
        CmdPacket.__init__(self, Cmd.VALVE_STATE.value)

        if not Valve.has_value(valve):
            raise ValueError("Invalid valve ID")
        if not ValveState.has_value(state):
            raise ValueError("Invalid valve state")

        self.valve = valve
        self.state = state
        self.num_padding -= 2

        self.pack_cmd(self)

    def pack_cmd(self):
        """Pack fields into byte form for transmission over USB"""
        self.packed_bytes += struct.pack('<BB', self.valve, self.state)
        self.packed_bytes += struct.pack('<{}x'.format(self.num_padding))  # Remaining payload
        self.pack_checksum(self)

    def print_with(self, print_func):
        CmdPacket.print_with(print_func)
        print_func("Valve:               {}\n".format(self.valve))
        print_func("State:               {}\n".format(self.state))


# Internal Packet Definitions #######################################################


class UsbCommand(object):
    """Command (from GUI to USB process) to enable/disable serial connection"""
    def __init__(self, conn):
        self.conn = conn

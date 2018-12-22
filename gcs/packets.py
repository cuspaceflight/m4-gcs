"""
USB packet definitions
CUSF 2018/19
"""

import json
import struct
import time
from enum import Enum


def fletcher32(bytes_arg):
    """Source: azbshiri (https://gist.github.com/globby/9337839)"""
    a = struct.unpack("<{}B".format(len(bytes_arg)), bytes_arg)
    b = [sum(a[:i])%65535 for i in range(len(a)+1)]
    return ((sum(b)%65535 << 16) | max(b))


# Current packet variables:       data_struct : Raw packet data (save just in case it's needed later)
#                                 packet_type : What data is contained in packet
#                                 timestamp   : When the data was received
#                                 data        : actual data contained.
# Input data structure: 128 bytes, of which the first 8 bytes are meta data.
# Meta data structure : Byte 0   : packet_type
#                       Byte 1-3 : RESERVED
#                       Byte 4-7 : timestamp

# RX Packets ########################################################################
# Constants:
# TODO:check constants
RX_PCKT_SIZE = 128
PAYLOAD_START = 8
PAYLOAD_END = RX_PCKT_SIZE - 4
CHANNEL_STATUS_SIZE = 8


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
    UPDATE_CONFIG = 0xF2

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
    MAIN_VALVE = 0xA6

    B_CH1 = 0xB1
    B_CH2 = 0xB2
    B_CH3 = 0xB3
    B_CH4 = 0xB4
    B_CH5 = 0xB5
    IGNITER = 0xB6

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


class Packet(object):
    """Base class"""
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""

        self.data_struct = input_struct

        meta_data = struct.unpack('<BBBBI', self.data_struct[0:PAYLOAD_START])

        self.type = meta_data[0]
        self.timestamp = meta_data[4]

        # Fletcher-32 checksum
        self.checksum = struct.unpack('<I', self.data_struct[PAYLOAD_END:RX_PCKT_SIZE])

        # Calculate checksum and ensure it matches self.checksum, store result in self.valid bool
        self.checksum_calc = fletcher32(self.data_struct[:PAYLOAD_END])
        self.valid = (self.checksum_calc == self.checksum)

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        # TODO: print packet to a pyqt text box in the gui

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""

        # TODO: print packet to text file in readable format
        # e.g.: filename.write("\n\n<attribute name>: {}\n".format(self.<attribute>))

        filename.write("\nPacket ID = {}   , Timestamp = {}".
                       format(self.type, self.timestamp))

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        # TODO: form a dict from packet and json.dump into 'filename'
        pass

    def print_to_terminal(self):
        print("\n\n")
        print("\nType:                {}".format(self.type))
        print("\nTimestamp:           {}".format(self.timestamp))
        print("\nReceived checksum:   {}".format(self.checksum))
        print("\nCalculated checksum: {}".format(self.checksum_calc))


class BankStatusPacket(Packet):
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        Packet.__init__(self, input_struct)

        payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]

        bank_status = struct.unpack('<BBHHH', payload[0:8])
        # Todo: add comments with units for each
        self.bank = bank_status[0]
        self.state = bank_status[1]
        self.psu_v = bank_status[2]
        self.firing_v = bank_status[3]
        self.firing_c = bank_status[4]

    # Todo: override methods from base Packet class (e.g. printout)
    # E.g.:
    def print_to_terminal(self):
        Packet.print_to_terminal()
        print("\nBank:           {}".format(self.bank))
        print("\nState:          {}".format(self.state))
        print("\nPSU Voltage:    {}".format(self.psu_v))
        print("\nFiring Voltage: {}".format(self.firing_v))
        print("\nFiring Current: {}".format(self.firing_c))


class ChannelStatus(object):
    """Not a packet, but a component of ChannelStatusPacket"""

    def __init__(self, input_struct=bytes(CHANNEL_STATUS_SIZE)):
        """Unpack incoming bytes

        input_struct -- incoming bytes to be unpacked"""
        channel_status = struct.unpack('<HHHH', input_struct)  # Todo: check format of each field
        # Todo: add comments with units for each
        self.firing_v = channel_status[0]
        self.output_v = channel_status[1]
        self.output_c = channel_status[2]
        self.resistance = channel_status[3]

    # Todo: override methods from base Packet class (e.g. printout)
    # E.g.:
    def print_to_terminal(self):
        print("\nFiring Voltage: {}".format(self.firing_v))
        print("\nOutput Voltage: {}".format(self.output_v))
        print("\nOutput Current: {}".format(self.output_c))
        print("\nResistance:     {}".format(self.resistance))


class ChannelStatusPacket(Packet):
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        Packet.__init__(self, input_struct)

        payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]
        self.bank = struct.unpack('<B', payload[0])  # Todo: check format of bank field
        self.channel_status = []
        for i in range(0, 5):
            self.channel_status.append(ChannelStatus(payload[i * CHANNEL_STATUS_SIZE:(i + 1) * CHANNEL_STATUS_SIZE]))

    # Todo: override methods from base Packet class (e.g. printout)
    # E.g.:
    def print_to_terminal(self):
        print("\nBank: {}".format(self.bank))
        for i in range(0, 5):
            print("\n\nChannel{}".format(i))
            self.channel_status[i].print_to_terminal()


# # Event Packets #####################################################################
# class Event(Enum):
#     a = 1
#     # Todo: fill in, ack messages use same ID as command
#
#
# event_list = [ev.value for ev in Event]
#
#
# class EventPacket(object):
#     def __init__(self, input_struct=bytes(EVENT_PACKET_SIZE)):
#         """Form packet from incoming USB bytes
#
#         input_struct -- incoming packet in raw bytes form"""
#
#         self.data_struct = input_struct
#
#         data = struct.unpack('<BIBBBB', self.data_struct)
#
#         self.id = data[0]
#         self.timestamp = data[1]
#
#         # Fletcher-32 checksum
#         self.checksum = data[2:6]
#         # Todo: calculate checksum and ensure it matches self.checksum, store result in self.valid bool
#
#     def printout(self, textbox):
#         """Print packet in the gui
#
#         textbox -- PyQt text box to print to"""
#         # TODO: print packet to a pyqt text box in the gui
#
#     def print_to_file(self, filename):
#         """Log packet in human readable text file
#
#         filename -- absolute path to .txt log file"""
#
#         # TODO: print packet to text file in readable format
#         # e.g.: filename.write("\n\n<attribute name>: {}\n".format(self.<attribute>))
#
#     def print_to_js(self, filename):
#         """ Log packet in json file
#
#         filename -- absolute path to .json log file"""
#         # TODO: form a dict from packet and json.dump into 'filename'
#         pass


# Tx Packets ########################################################################

class CmdPacket(object):
    """Base PC to valve controller command packet"""
    def __init__(self, cmd):
        if not Cmd.has_value(cmd):
            raise ValueError("Invalid command ID")
        self.cmd = cmd
        self.timestamp = int(round(time.time()))
        self.packed_bytes = struct.pack('<B3xIB', PcktTypes.CMD.value, self.timestamp, self.cmd)
        self.checksum = 0
    def pack_cmd(self):
        self.packed_bytes += struct.pack('<{}x'.format(115), zeros)  # Remaining payload
        self.calc_checksum()

    def calc_checksum(self):
        # Calculate checksum and ensure it matches self.checksum, store result in self.valid bool
        self.checksum = fletcher32(self.packed_bytes)
        self.packed_bytes += struct.pack('<I', self.checksum)  # Checksum


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

        self.pack_cmd()

    def pack_cmd(self):
        self.packed_bytes += struct.pack('<BB', self.bank, self.state)
        self.packed_bytes += struct.pack('<{}x'.format(113))  # Remaining payload
        CmdPacket.calc_checksum(self)


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

        self.pack_cmd()

    def pack_cmd(self):
        self.packed_bytes += struct.pack('<BB', self.valve, self.state)
        self.packed_bytes += struct.pack('<{}x'.format(113))  # Remaining payload
        CmdPacket.calc_checksum(self)


class ConfigCmdPacket(CmdPacket):
    """Command to set valve-channel mapping config"""
    def __init__(self, supply_1, vent_1, supply_2, vent_2, ignitor):
        CmdPacket.__init__(self, Cmd.UPDATE_CONFIG.value)

        if not Valve.has_value(supply_1):
            raise ValueError("Invalid supply_1 valve ID")
        if not Valve.has_value(vent_1):
            raise ValueError("Invalid vent_1 valve ID")
        if not Valve.has_value(supply_2):
            raise ValueError("Invalid supply_2 valve ID")
        if not Valve.has_value(vent_2):
            raise ValueError("Invalid vent_2 valve ID")
        if not Valve.has_value(ignitor):
            raise ValueError("Invalid ignitor valve ID")

        self.supply_1 = supply_1
        self.vent_1 = vent_1
        self.supply_2 = supply_2
        self.vent_2 = vent_2
        self.ignitor = ignitor

        self.pack_cmd()

    def pack_cmd(self):
        self.packed_bytes += struct.pack('<BBBBB', self.supply_1, self.vent_1, self.supply_2, self.vent_2, self.ignitor)
        self.packed_bytes += struct.pack('<{}x'.format(110))  # Remaining payload
        CmdPacket.calc_checksum(self)

# Internal Packet Definitions #######################################################
class UsbCommand(object):
    """Command (from GUI to USB process) to enable/disable serial connection"""
    def __init__(self, conn):
        self.conn = conn

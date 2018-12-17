"""
USB packet definitions
CUSF 2018/19
"""

import json
import struct
import time
from enum import Enum


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
RX_PCKT_SIZE = 128  # TODO: number of bytes?
PAYLOAD_START = 8  # TODO: check
PAYLOAD_END = RX_PCKT_SIZE - 4
CHANNEL_STATUS_SIZE = 7
EVENT_PACKET_SIZE = 9


class Packet(object):
    """Base class"""
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""

        self.data_struct = input_struct

        meta_data = struct.unpack('<BBBBI', self.data_struct[0:PAYLOAD_START])

        self.packet_type = meta_data[0]
        self.timestamp = meta_data[4]

        # Fletcher-32 checksum
        self.checksum = struct.unpack('<BBBB', self.data_struct[PAYLOAD_END:RX_PCKT_SIZE])

        # Todo: calculate checksum and ensure it matches self.checksum, store result in self.valid bool

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
                       format(self.packet_type, self.timestamp))

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        # TODO: form a dict from packet and json.dump into 'filename'
        pass


class ChannelStatus(object):
    """Not a packet, but a component of ChannelStatusPacket"""
    def __init__(self, input_struct=bytes(CHANNEL_STATUS_SIZE)):
        """Unpack incoming bytes

        input_struct -- incoming bytes to be unpacked"""
        channel_status = struct.unpack('<HHHB', input_struct)  # Todo: check format of each field
        # Todo: add comments with units for each
        self.firing_v = channel_status[0]
        self.output_v = channel_status[1]
        self.output_c = channel_status[2]
        self.continuity = channel_status[3]


class ChannelStatusPacket(Packet):
        def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
            """Form packet from incoming USB bytes

            input_struct -- incoming packet in raw bytes form"""
            Packet. __init__(self, input_struct)

            payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]
            self.bank = struct.unpack('<B', payload[0])  # Todo: check format of bank field
            channel_status = []
            for i in range(0, 5):
                channel_status.append(ChannelStatus(payload[i*CHANNEL_STATUS_SIZE:(i+1)*CHANNEL_STATUS_SIZE]))

        # Todo: override methods from base Packet class (e.g. printout)


class BankStatusPacket(Packet):
    def __init__(self, input_struct=bytes(RX_PCKT_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        Packet.__init__(self, input_struct)

        payload = self.data_struct[PAYLOAD_START:PAYLOAD_END]
        bank_status = struct.unpack('<BHHHB', payload[0:8])  # Todo: check format of each field
        # Todo: add comments with units for each
        self.bank = bank_status[0]
        self.psu_v = bank_status[1]
        self.firing_v = bank_status[2]
        self.firing_c = bank_status[3]
        self.controller_state = bank_status[4]

        # Todo: override methods from base Packet class (e.g. printout)

# Event Packets #####################################################################
class Event(Enum):
    a = 1
    # Todo: fill in, ack messages use same ID as command


event_list = [ev.value for ev in Event]


class EventPacket(object):
    def __init__(self, input_struct=bytes(EVENT_PACKET_SIZE)):
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""

        self.data_struct = input_struct

        data = struct.unpack('<BIBBBB', self.data_struct)

        self.id = data[0]
        self.timestamp = data[1]

        # Fletcher-32 checksum
        self.checksum = data[2:6]
        # Todo: calculate checksum and ensure it matches self.checksum, store result in self.valid bool

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        # TODO: print packet to a pyqt text box in the gui

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""

        # TODO: print packet to text file in readable format
        # e.g.: filename.write("\n\n<attribute name>: {}\n".format(self.<attribute>))

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        # TODO: form a dict from packet and json.dump into 'filename'
        pass


# Tx Packets ########################################################################
class Cmd(Enum):
    ENERGIZE_BANK = 1
    ARM_BANK      = 2
    FIRE_VALVE    = 3
    UPDATE_CONFIG = 4


cmd_list = [cmd.value for cmd in Cmd]


class CmdPacket(object):
    """Base PC to valve controller command packet"""
    def __init__(self, cmd):
        if cmd not in cmd_list:
            self.valid = False
        else:
            self.valid = True
        self.id = cmd
        self.timestamp = int(round(time.time()))
        # Todo: calculate Fletcher-32 checksum then uncomment and finish line below
        #self.packed_bytes = struct.pack('<BIBBBB', self.id, self.timestamp <insert x4 checksum bytes here>)


# Internal Packet Definitions #######################################################
class UsbCommand(object):
    """Command (from GUI to USB process) to enable/disable serial connection"""
    def __init__(self, conn):
        self.conn = conn

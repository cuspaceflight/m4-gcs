"""
USB packet definitions
CUSF 2018/19
"""

import json
import struct


# Current packet variables:       data_struct : Raw packet data (save just in case it's needed later)
#                                 packet_type : What data is contained in packet
#                                 timestamp   : When the data was received
#                                 data        : actual data contained.
# Input data structure: 128 bytes, of which the first 8 bytes are meta data.
# Meta data structure : Byte 0   : packet_type
#                       Byte 1-3 : RESERVED
#                       Byte 4-7 : timestamp


class Packet(object):
    """Base class"""
    def __init__(self, input_struct=bytes(128)):  # TODO: number of bytes?
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""

        self.data_struct = input_struct

        meta_data = struct.unpack('<BBBBI', self.data_struct[0:8])

        self.packet_type = meta_data[0]
        self.timestamp = meta_data[4]
        self.data = self.data_struct[8:128]

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        # TODO: print packet to a pyqt text box in the gui

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""



        # TODO: print packet to text file in readable format
        # e.g.: filename.write("\n\n<attribute name>: {}\n".format(self.<attribute>))

        filename.write("\nPacket ID = {}   , Timestamp = {}   , Data = {}".
                       format(self.packet_type, self.timestamp, self.data))

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        # TODO: form a dict from packet and json.dump into 'filename'
        pass


# Packets to Transmit #
class CmdPacket(object):
    """Base PC to valve controller command packet"""
    def __init__(self, cmd):
        self.cmd = cmd

        self.packed_bytes = struct.pack('<B', self.cmd)


# Internal Packet Definitions #
class UsbCommand(object):
    """Command (from GUI to USB process) to enable/disable serial connection"""
    def __init__(self, conn):
        self.conn = conn

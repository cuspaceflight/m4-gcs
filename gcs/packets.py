"""
USB packet definitions
CUSF 2018/19
"""

import json

# TODO:
#     - Define packets used to communicate with the firing controller


class Packet(object):
    """Base class"""
    def __init__(self, input_struct=bytes(128)):  # TODO: number of bytes?
        """Form packet from incoming USB bytes

        input_struct -- incoming packet in raw bytes form"""
        self.data_struct = input_struct

        # TODO: unpack packet, e.g.:
            # meta_data = struct.unpack('<BBI', self.data_struct[0:6])
            # self.log_type = meta_data[0]
            # self.toad_id = meta_data[1]
            # self.systick = meta_data[2]  # systicks
            # self.systick_freq = 10000  # Hz
            # self.timestamp = self.systick / self.systick_freq  # s

    def printout(self, textbox):
        """Print packet in the gui

        textbox -- PyQt text box to print to"""
        # TODO: print packet to a pyqt text box in the gui

    def print_to_file(self, filename):
        """Log packet in human readable text file

        filename -- absolute path to .txt log file"""
        # TODO: print packet to text file in readable format
        # e.g.: filename.write("\n\n<attribute name>: {}\n".format(self.<attribute>))
        pass

    def print_to_js(self, filename):
        """ Log packet in json file

        filename -- absolute path to .json log file"""
        # TODO: form a dict from packet and json.dump into 'filename'
        pass

"""
Created on 27 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys

from scs_core.sys.process_comms import ProcessComms


# --------------------------------------------------------------------------------------------------------------------

class StdIO(ProcessComms):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def read(self):
        for line in sys.stdin:
            yield line


    def write(self, message, wait_for_availability=True):
        print(message)


    def close(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
            return "StdIO:{}"

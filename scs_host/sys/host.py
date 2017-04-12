"""
Created on 20 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os


# --------------------------------------------------------------------------------------------------------------------

class Host(object):
    """
    Any Darwin Mac
    """

    __SCS_OSIO = 'SCS/osio/'      # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def osio_dir(cls):
        return os.path.expanduser('~') + '/' + cls.__SCS_OSIO

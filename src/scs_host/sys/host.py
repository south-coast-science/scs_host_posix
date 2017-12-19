"""
Created on 20 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname
"""

import os
import socket

from scs_core.sys.node import Node


# --------------------------------------------------------------------------------------------------------------------

class Host(Node):
    """
    Any Darwin Mac
    """

    __SCS =         'SCS/'              # hard-coded path

    __SCS_CONF =    'conf/'             # hard-coded path
    __SCS_AWS =     'aws/'              # hard-coded path
    __SCS_OSIO =    'osio/'             # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def name(cls):
        full_name = socket.gethostname()
        full_names = full_name.split('.')

        return full_names[0]


    @classmethod
    def scs_dir(cls):
        return os.path.expanduser('~') + '/' + cls.__SCS


    @classmethod
    def conf_dir(cls):
        return os.path.expanduser('~') + '/' + cls.__SCS + cls.__SCS_CONF


    @classmethod
    def aws_dir(cls):
        return os.path.expanduser('~') + '/' + cls.__SCS + cls.__SCS_AWS


    @classmethod
    def osio_dir(cls):
        return os.path.expanduser('~') + '/' + cls.__SCS + cls.__SCS_OSIO

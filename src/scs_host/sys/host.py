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
    Any Darwin Mac or Linux
    """

    __CONF_DIR =            "SCS/conf/"                         # hard-coded rel path
    __AWS_DIR =             "SCS/aws/"                          # hard-coded rel path
    __OSIO_DIR =            "SCS/osio/"                         # hard-coded rel path


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def name(cls):
        full_name = socket.gethostname()
        full_names = full_name.split('.')

        return full_names[0]


    @classmethod
    def ndir_spi_bus(cls):
        raise NotImplementedError


    @classmethod
    def ndir_spi_device(cls):
        raise NotImplementedError


    @classmethod
    def opc_spi_bus(cls):
        raise NotImplementedError


    @classmethod
    def opc_spi_device(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def home_dir(cls):
        return os.path.expanduser('~') + '/'


    @classmethod
    def lock_dir(cls):
        raise NotImplementedError


    @classmethod
    def tmp_dir(cls):
        raise NotImplementedError


    @classmethod
    def command_dir(cls):
        raise NotImplementedError


    @classmethod
    def conf_dir(cls):
        return cls.home_dir() + cls.__CONF_DIR


    @classmethod
    def aws_dir(cls):
        return cls.home_dir() + cls.__AWS_DIR


    @classmethod
    def osio_dir(cls):
        return cls.home_dir() + cls.__OSIO_DIR


    @classmethod
    def eep_image(cls):
        raise NotImplementedError

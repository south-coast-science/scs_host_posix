"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: only one reader per UDS! Reader must be started before writer.
Note: multiple writers are permitted per UDS.

https://pymotw.com/2/socket/uds.html
"""

import os
import socket
import time

from scs_core.sys.process_comms import ProcessComms


# --------------------------------------------------------------------------------------------------------------------

class UDS(ProcessComms):
    """
    classdocs
    """

    __BACKLOG = 1
    __BUFFER_SIZE = 255


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def __read(cls, connection):
        message = b''

        while True:
            data = connection.recv(cls.__BUFFER_SIZE)

            if not data:
                break

            message += data

        return message


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, address):
        """
        Constructor
        """
        self.__address = address
        self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


    # ----------------------------------------------------------------------------------------------------------------

    def read(self):         # warning: blocks forever
        try:
            os.unlink(self.__address)
        except OSError:
            if os.path.exists(self.__address):
                raise

        # socket...
        self.__socket.bind(self.__address)
        self.__socket.listen(UDS.__BACKLOG)

        while True:
            connection, _ = self.__socket.accept()

            try:
                # data...
                yield UDS.__read(connection).decode().strip()

            finally:
                connection.close()


    def write(self, message, wait_for_availability=True):       # TODO: should be co-routine?
        while True:
            try:
                # socket...
                self.__socket.connect(self.__address)
                break
            except socket.error:
                if not wait_for_availability:
                    raise

                time.sleep(0.1)

        try:
            # data...
            self.__socket.sendall(message.encode())

        finally:
            self.__socket.close()


    def close(self):
        if self.__socket:
            self.__socket.close()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
            return "UDS:{address:%s, socket:%s}" % (self.__address, self.__socket)

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


# TODO: create a common comms abstraction?

# --------------------------------------------------------------------------------------------------------------------

class UDS(object):
    """
    classdocs
    """

    __BACKLOG = 1
    __BUFFER_SIZE = 255


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, address):
        """
        Constructor
        """
        self.__address = address
        self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


    # ----------------------------------------------------------------------------------------------------------------

    def read(self):         # blocks forever
        # socket...
        try:
            # socket already exists?
            os.unlink(self.__address)
        except OSError:
            if os.path.exists(self.__address):
                raise

        self.__socket.bind(self.__address)
        self.__socket.listen(UDS.__BACKLOG)

        # data...
        while True:
            connection, _ = self.__socket.accept()

            try:
                message = b''

                while True:
                    data = connection.recv(UDS.__BUFFER_SIZE)

                    if not data:
                        break

                    message += data

                yield message.decode().strip()

            finally:
                connection.close()


    def write(self, message, wait_for_availability=True):       # TODO: should be co-routine?
        # socket...
        while True:
            try:
                self.__socket.connect(self.__address)
                break
            except socket.error:
                if not wait_for_availability:
                    raise

                time.sleep(0.1)

        # data...
        try:
            self.__socket.sendall(message.encode())

        finally:
            self.__socket.close()


    def close(self):
        if self.__socket:
            self.__socket.close()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
            return "UDS:{address:%s, socket:%s}" % (self.__address, self.__socket)

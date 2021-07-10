#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://pymotw.com/2/socket/uds.html
"""

import socket
import sys
import os


# --------------------------------------------------------------------------------------------------------------------

server_address = './test_socket.uds'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise


# Create a UDS socket
sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)


# Bind the socket to the port
print('starting up on %s' % server_address, sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('connection from %s' % client_address, sys.stderr)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received %s' % data, sys.stderr)

            if data:
                print('sending data back to the client', sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from %s' % client_address, sys.stderr)
                break

    finally:
        # Clean up the connection
        connection.close()

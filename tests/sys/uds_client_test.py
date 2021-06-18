#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://pymotw.com/2/socket/uds.html
"""

import socket
import sys


# --------------------------------------------------------------------------------------------------------------------

# Create a UDS socket
sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './test_socket.uds'

print('connecting to %s' % server_address, sys.stderr)

try:
    sock.connect(server_address)
except socket.error as sock_error:
    print(sock_error)
    sys.exit(1)


try:
    # Send data
    message = b"This is the message.  It will be repeated."

    print('sending %s' % message, sys.stderr)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)

        print('received %s' % data, sys.stderr)

finally:
    print('closing socket', sys.stderr)
    sock.close()

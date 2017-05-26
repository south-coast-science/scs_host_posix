#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: multiple writers are permitted per UDS.

https://pymotw.com/2/socket/uds.html
"""

from scs_host.sys.uds import UDS


# --------------------------------------------------------------------------------------------------------------------

server_address = './test_socket.uds'

uds = UDS(server_address)
print(uds)

try:
    uds.write("Hello UDS!")

finally:
    uds.close()     # not needed - just to check a closed connection can be closed

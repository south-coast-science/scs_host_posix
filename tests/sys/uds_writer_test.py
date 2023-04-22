#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: multiple writers are permitted per UDS.

https://pymotw.com/2/socket/uds.html
"""

import time

from scs_host.comms.domain_socket import DomainSocket


# --------------------------------------------------------------------------------------------------------------------

server_address = '/Users/bruno/Python/Mac/scs_analysis/scs_analysis/aws_mqtt_sub.uds'

uds = DomainSocket(server_address)
print(uds)

while True:
    try:
        uds.connect()
        uds.write("Hello UDS!")

    finally:
        uds.close()     # not needed - just to check a closed connection can be closed

    time.sleep(1)

#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: multiple writers are permitted per UDS.

https://pymotw.com/2/socket/uds.html
"""

import time

from scs_host.sys.uds import UDS


# --------------------------------------------------------------------------------------------------------------------

server_address = '/Users/bruno/Python/Mac/scs_analysis/scs_analysis/osio_mqtt_sub.uds'

uds = UDS(server_address)
print(uds)

while True:
    try:
        uds.connect()
        uds.write("Hello UDS!", False)

    finally:
        uds.close()     # not needed - just to check a closed connection can be closed

    time.sleep(1)
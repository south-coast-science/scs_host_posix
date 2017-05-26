#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: only one reader per UDS! Reader must be started before writer.

https://pymotw.com/2/socket/uds.html
"""

import sys

from scs_core.data.localized_datetime import LocalizedDatetime

from scs_host.sys.uds import UDS


# --------------------------------------------------------------------------------------------------------------------

server_address = './test_socket.uds'

uds = UDS(server_address)
print(uds)

try:
    for message in uds.read():
        now = LocalizedDatetime.now()
        print("%s: got:[%s]" % (now.as_iso8601(), message))

except KeyboardInterrupt as ex:
    print("uds_reader_test: KeyboardInterrupt", file=sys.stderr)

finally:
    uds.close()

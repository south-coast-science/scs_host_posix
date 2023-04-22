#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: only one reader per UDS! Reader must be started before writer.

https://pymotw.com/2/socket/uds.html
"""

import sys

from scs_core.data.datetime import LocalizedDatetime

from scs_host.comms.domain_socket import DomainSocket


# --------------------------------------------------------------------------------------------------------------------

server_address = '/Users/bruno/Python/Mac/scs_analysis/scs_analysis/aws_mqtt_sub.uds'

uds = DomainSocket(server_address)
print(uds)

try:
    uds.connect()

    for message in uds.read():
        now = LocalizedDatetime.now()
        print("%s: got:[%s]" % (now.as_iso8601(), message))

except KeyboardInterrupt:
    print(file=sys.stderr)

finally:
    uds.close()

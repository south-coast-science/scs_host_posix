#!/usr/bin/env python3

"""
Created on 16 Apr 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

path = '/Users/bruno'
usage = Host.disk_usage(path)
print("path: %s usage: %s" % (path, usage))

print(JSONify.dumps(usage.as_json()))
print("-")


path = '/Volumes/SCS'
usage = Host.disk_usage(path)
print("path: %s usage: %s" % (path, usage))

print(JSONify.dumps(usage.as_json()))
print("-")


path = '/Volumes/non-existent'
usage = Host.disk_usage(path)
print("path: %s usage: %s" % (path, usage))

print(JSONify.dumps(usage.as_json()))
print("-")


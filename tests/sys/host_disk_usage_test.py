#!/usr/bin/env python3

"""
Created on 16 Apr 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify

from scs_host.sys.host import Host


# TODO: add disk usage command to scs_mfr

# --------------------------------------------------------------------------------------------------------------------

volume = '/Users/bruno'
usage = Host.disk_usage(volume)
print("volume: %s usage: %s" % (volume, usage))

print(JSONify.dumps(usage.as_json()))
print("-")

volume = '/'
usage = Host.disk_usage(volume)
print("volume: %s usage: %s" % (volume, usage))

print(JSONify.dumps(usage.as_json()))
print("-")


volume = '/Volumes/non-existent'
usage = Host.disk_usage(volume)
print("volume: %s usage: %s" % (volume, usage))

print(JSONify.dumps(usage.as_json()))

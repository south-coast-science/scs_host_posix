#!/usr/bin/env python3

"""
Created on 2 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

home_path = Host.home_path()
print("home_path: %s" % home_path)

scs_path = Host.scs_path()
print("scs_path: %s" % scs_path)

print("-")

conf_dir = Host.conf_dir()
print("conf_dir: %s" % conf_dir)

aws_dir = Host.aws_dir()
print("aws_dir: %s" % aws_dir)

osio_dir = Host.osio_dir()
print("osio_dir: %s" % osio_dir)

print("-")

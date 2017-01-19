#!/usr/bin/env python3

"""
Created on 9 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import http.client


# --------------------------------------------------------------------------------------------------------------------

conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
print(data1)


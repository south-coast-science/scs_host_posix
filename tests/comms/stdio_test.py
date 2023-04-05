#!/usr/bin/env python3

"""
Created on 26 Apr 2021

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os
import sys

from scs_host.comms.stdio import StdIO


# --------------------------------------------------------------------------------------------------------------------

filename = os.path.expanduser('~/stdio_test_history')
vocabulary = ['dog', 'cat', 'rabbit', 'bird', 'slug', 'snail', 'exit']

try:
    StdIO.set(history_filename=filename, vocabulary=vocabulary)

    while True:
        line = StdIO.prompt('test')
        print("line: %s" % line)
        print("-")

        if line == 'exit':
            break

except (EOFError, KeyboardInterrupt):
    print(file=sys.stderr)

finally:
    StdIO.save_history(filename)

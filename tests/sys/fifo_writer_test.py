#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: multiple writers are permitted per fifo.

https://stackoverflow.com/questions/7048095/how-do-i-properly-write-to-fifos-in-python
"""

import sys


# --------------------------------------------------------------------------------------------------------------------

fifo_writer = None

try:
    fifo_writer = open('test_pipe.fifo', 'w')        # warning: blocks until there is a reader

    print("writing...")

    sys.stdout.write("Hello writer!" + "\n")
    sys.stdout.flush()

    fifo_writer.write("Hello writer!" + "\n")
    fifo_writer.flush()


finally:
    if fifo_writer:
        fifo_writer.close()

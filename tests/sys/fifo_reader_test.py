#!/usr/bin/env python3

"""
Created on 26 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Note: only one reader per fifo!

https://stackoverflow.com/questions/7048095/how-do-i-properly-write-to-fifos-in-python
"""

import sys
import time


# --------------------------------------------------------------------------------------------------------------------

fifo_reader = None

try:
    fifo_reader = open('test_pipe.fifo')

    print("reading...")

    while True:                     # we need this loop because the fifo reader stream ends when the writer terminates
        for line in fifo_reader:
            print("[%s]" % line.strip())
            sys.stdout.flush()

        time.sleep(0.1)             # required to prevent a tight loop


except KeyboardInterrupt:
    print(file=sys.stderr)

finally:
    if fifo_reader:
        fifo_reader.close()

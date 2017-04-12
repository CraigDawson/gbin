#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage: forever.py command args
"""

import sys
import time
import subprocess


def main():
    try:
        cmd = ' '.join(sys.argv[1:])

        i = 1
        while True:
            print '=== Iteration {} ==='.format(i)
            status = subprocess.call(cmd, shell=True)
            print '=== exit status {} ==='.format(status)
            i += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print '^C detected'


if __name__ == '__main__':
    main()

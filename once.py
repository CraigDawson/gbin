#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage: once.py command args
"""

import sys
import subprocess
import big_letters


def main():
    try:
        cmd = ' '.join(sys.argv[1:])

        status = subprocess.call(cmd, shell=True)
        print '=== exit status {} ==='.format(status)
        if not status:
            big_letters.print_big('XXX  DONE  XXX')
        else:
            big_letters.print_big('XXX ERROR XXX')

    except KeyboardInterrupt:
        print ' === User abort detected === '

if __name__ == '__main__':
    main()

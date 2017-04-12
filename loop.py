#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage: loop.py N command args
"""

import sys
import subprocess
import big_letters


def main():
    num = sys.argv[1]
    cmd = ' '.join(sys.argv[2:])

    for i in range(int(num)):
        print '=== Iteration {} ==='.format(i + 1)
        status = subprocess.call(cmd, shell=True)
        print '=== exit status {} ==='.format(status)

    big_letters.print_big('XXX  DONE  XXX')


if __name__ == '__main__':
    main()

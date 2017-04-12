#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage: whileSuccess.py command args
"""

import sys
import time
import subprocess
import os.path
import os
import big_letters


def main():
    try:
        cmd = ' '.join(sys.argv[1:])

        status = 0
        i = 1
        while not status:
            print '=== Iteration {} ==='.format(i)
            status = subprocess.call(cmd, shell=True)
            print '=== exit status {} ==='.format(status)
            i += 1
            if os.path.isfile('stop_loop'):
                big_letters.print_big('XXX  DONE  XXX')
                os.remove('stop_loop')
                break
            time.sleep(1)
        else:
            big_letters.print_big('XXX ERROR XXX')
    except KeyboardInterrupt:
        print ' === User abort detected === '


if __name__ == '__main__':
    main()

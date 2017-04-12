#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def convert_to_d_h_m_s(seconds):
    """ Return the tuple of days, hours, minutes and seconds. """

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return days, hours, minutes, seconds


def do_convert(secs):
    seconds = int(secs)
    print("{0:12d} seconds: {1[0]:12d}:{1[1]:02d}:{1[2]:02d}:{1[3]:02d}".format(
        seconds, convert_to_d_h_m_s(seconds)))


def main(argv):
    if len(sys.argv) > 1:
        for secs in argv[1:]:
            do_convert(float(secs))
    else:
        print 'Usage: {} secs1 secs2 . . . secsN'.format(argv[0])
        print '       to convert secs to d:hh:mm:ss'

if __name__ == "__main__":
    main(sys.argv)

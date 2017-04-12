#!/usr/bin/python

import sys
import os
from shutil import move
from shutil import rmtree


def cdbk(full):

    def addExt(path, ext):
        return path + ext

    last = addExt(full, ".last")
    old = addExt(full, ".old")

    try:
        print last, " -> ", old
        if os.path.isdir(old):
            rmtree(old)
        move(last, old)
    except IOError as e:
        print e

    try:
        print full, " -> ", last
        if os.path.isdir(last):
            rmtree(last)
        move(full, last)

    except IOError as e:
        print e

    return True


if len(sys.argv) != 2:
    print "Usage: ", sys.argv[0], " filename"
    sys.exit(2)


if not cdbk(sys.argv[1]):
    print "Error backing up ", sys.argv[1]

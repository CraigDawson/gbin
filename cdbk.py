#!/usr/bin/python

import sys
import os
from shutil import copy


def cdbk(full):
    
    def addExt(path, ext):
        return path + ext

    last = addExt(full, ".last")
    old  = addExt(full, ".old")

    if not os.path.isfile(full):
        return False 

    if os.path.isfile(last):
        print last, " -> ", old
        copy(last, old)

    print full, " -> ", last
    copy(full, last)

    return True


if len(sys.argv) != 2:
    print "Usage: ", sys.argv[0], " filename"
    sys.exit(2)


if not cdbk(sys.argv[1]):
    print "Error backing up ", sys.argv[1]



#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import shutil


def copyFile(old, new):
    '''
    rename or copy file?
    Only if new doesn't exist
    '''
    if os.path.isfile(new):
        print 'File {} already exists!'.format(new)
        sys.exit(1)

    try:
        shutil.copyfile(old, new)
    except IOError as e:
        print e
        sys.exit(1)


def addRev(file_name):
    '''
    Add rev before .ext
    '''
    # split out 1st or only ext
    (fn, ext) = os.path.splitext(file_name)

    # if no ext then add _r1 and be done
    if ext is '':
        new_file_name = ''.join((fn, '_r1'))
    else:
        new_file_name = ''.join((fn, '_r1', ext))

    copyFile(file_name, new_file_name)
    print '{} -> {}'.format(file_name, new_file_name)


def updateRev(file_name, new_rev):
    '''
    Update revision
    '''
    p = re.compile(r'_r(\d+)')
    new_file_name = p.sub(''.join(['_r', str(new_rev)]), file_name)
    copyFile(file_name, new_file_name)
    print '{} -> {}'.format(file_name, new_file_name)


def main():
    try:
        fn = sys.argv[1]
    except IndexError:
        print 'Usage: {} file_name'.format(sys.argv[0])
        sys.exit(1)

    p = re.compile(r'_r(\d+)')
    m = p.search(fn)
    if not m:
        addRev(fn)
        sys.exit(0)

    rev = int(m.group(1))
    rev += 1
    updateRev(fn, rev)


if __name__ == '__main__':
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
 This is rev _r2 of cdrup.py

 It increments N in '_rN' in the first 10 lines of a text/src file.

'''

from __future__ import print_function

import better_exceptions
import sys
import re
import fileinput


def updateRev(line, p):
    '''
    Update revision if available
    '''
    m = p.search(line)
    if not m:
        return line

    rev = int(m.group(1))
    rev += 1

    line = p.sub(''.join(['_r', str(rev)]), line)

    return line


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def process(line, lineno, p):
    if lineno > 10:
        return line

    line = updateRev(line, p)
    eprint('{:02d}) {}'.format(lineno, line), end='')
    return line


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 2:
        print('Usage: {} file_name . . .'.format(sys.argv[0]))
        return 1

    p = re.compile(r'_r(\d+)')
    for line in fileinput.input(inplace=True, backup='.bak'):
        line = process(line, fileinput.lineno(), p)
        print(line, end='')

    return 0

if __name__ == '__main__':
    sys.exit(main())

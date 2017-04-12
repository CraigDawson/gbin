#!/usr/bin/env python

import psutil


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name == 'percent':
            print int(value)


def main():
    pprint_ntuple(psutil.virtual_memory())

if __name__ == '__main__':
    main()

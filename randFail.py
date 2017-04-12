#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import random


def main():
    n = random.uniform(0.0, 1.0)
    if n <= 0.5:
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main()

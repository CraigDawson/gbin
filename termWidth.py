#!/usr/bin/python
from __future__ import print_function

import os

rows, columns = os.popen('stty size', 'r').read().split()
print('Terminal size: {}, {}'.format(rows, columns))
cols = int(columns) // 10
print('cols={}'.format(cols))
pad = ' ' * 9
for n in range(1, cols + 1):
    print('{}{}'.format(pad, n % 10), end='')
print('')
print("123456789|" * cols, end='')
r = int(columns) % 10
if r:
    print('{}'.format('123456789'[:r]))
print('')

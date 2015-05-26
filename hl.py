#!/usr/bin/python
import os
rows, columns = os.popen('stty size', 'r').read().split()
print "\033(0\x71\033(B" * int(columns)


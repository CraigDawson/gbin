#!/usr/bin/python
import os
rows, columns = os.popen('stty size', 'r').read().split()
# \033[0;37m is White
print "\033[1;32m\033(0\x71\033(B\033[00m" * int(columns)

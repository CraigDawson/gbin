#!/usr/bin/env python
import sys
from termcolor import colored

i = 0
for line in sys.stdin:
    if i < 3:
        sys.stdout.write(colored(line, "green"))
    else:
        sys.stdout.write(line)

    i += 1

    if i > 5:
        i = 0



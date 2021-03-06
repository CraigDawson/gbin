#!/usr/bin/env python

"""
Starts vim with several possible input formats.
Examples:
  v foo/bar/baz.c # full correct path
  v baz.c # finds baz.c and edits the first
  v baz.c:123 # same but start at line 123
  v baz.c +123 # same as above
"""

import os
import sys


def find_first(name, path):
    """Find first file on path."""
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments.")
        sys.exit(1)

    filename = args[0]
    line = ""

    if len(args) > 1:
        line = args[1]

    if ":" in filename:
        v = filename.split(":")
        filename = v[0]
        if v[1] == "+":
            line = v[1]
        else:
            line = "+" + v[1]

    # Find file if not found
    if not os.path.exists(filename):
        filename = find_first(filename, ".")

    # Still not found? Don't do it.
    if filename is None or not os.path.exists(filename):
        print("Could not find: %s" % " ".join(sys.argv[1:]))
        sys.exit(1)

    cmd = "%s %s %s" % ("vim", filename, line)
    print(cmd)
    os.system(cmd)
    #%

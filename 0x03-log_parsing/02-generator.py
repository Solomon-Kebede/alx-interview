#!/usr/bin/python3

import sys

with open('file_5.txt') as f:
    lines = f.readlines()
    for line in lines:
        sys.stdout.write(line)
        sys.stdout.flush()
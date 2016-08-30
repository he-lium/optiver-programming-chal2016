#!/usr/bin/python3
import sys, string

for line in sys.stdin:
    sanitise = line.strip().lower()
    l = [c for c in sanitise if c in string.ascii_lowercase]
    if l == l[::-1]:
        print(line, end='')

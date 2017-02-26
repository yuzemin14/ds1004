#!/usr/bin/python

import sys

current_key = None
count = 1

for line in sys.stdin:
    line = line.strip()
    key, due = line.split('\t', 1)

    try:
        due = float(due)
        count += 1
    except ValueError:
        continue

    if current_key == key:
        total_due += due
    else:
        if current_key:
            print '%s\t%0.2f, %0.2f' % (current_key, total_due, total_due/(count-1))
        count = 1
        current_key = key
        total_due = due

if current_key == key:
    print '%s\t%0.2f, %0.2f' % (current_key, total_due, total_due/count)

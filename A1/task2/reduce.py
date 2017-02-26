#!/usr/bin/python

import sys

current_key = None

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_key == key:
        current_count += count
    else:
        if current_key:
            print '%s\t%d' % (current_key, current_count)
        current_count = count
        current_key = key

if current_key == key:
    print '%s\t%d' % (current_key, current_count)

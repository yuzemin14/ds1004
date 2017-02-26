#!/usr/bin/python

import sys

current_key = None
current_count = 0
max_count = 0

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
        if current_count > max_count:
            max_count = current_count
            max_key = current_key
        current_count = count
        current_key = key

if current_count > max_count:
    max_count = current_count
    max_key = current_key

print '%s\t%d' % (max_key, max_count)

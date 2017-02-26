#!/usr/bin/python

import sys

current_key = None

for line in sys.stdin:
    line = line.strip()
    key, weekend = line.split('\t', 1)

    try:
        weekend = int(weekend)
    except ValueError:
        continue

    if current_key == key:
        if weekend == 1:
            weekend_count += 1
        if weekend == 0:
            weekday_count += 1
    else:
        if current_key:
            print '%s\t%0.2f, %0.2f' % (current_key, weekend_count/8., weekday_count/23.)
        current_key = key
        if weekend == 1:
            weekend_count = 1
            weekday_count = 0
        if weekend == 0:
            weekend_count = 0
            weekday_count = 1

if current_key == key:
    print '%s\t%0.2f, %0.2f' % (current_key, weekend_count/8., weekday_count/23.)

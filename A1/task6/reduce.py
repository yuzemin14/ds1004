#!/usr/bin/python

import sys
from operator import itemgetter

counter = {}

for line in sys.stdin:
    line = line.strip()
    key, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if key in counter:
        counter[key] += count
    else:
        counter[key] = count

sorted_counter = sorted(counter.items(), key=itemgetter(1), reverse=True)

for k in sorted_counter[:20]:
    print '%s\t%d' % (k[0], k[1])

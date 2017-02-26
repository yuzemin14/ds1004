#!/usr/bin/python

import sys

current_key = None

for line in sys.stdin:
    end = 0
    line = line.strip()
    key, value = line.split('\t', 1)
    
    if current_key == None:
        current_key = key
        current_value = value
        end = 1
    elif current_key == key:
        current_key = None
        current_value = None
    else:
        if current_value != 'open':
            print '%s\t%s' % (current_key, current_value)
        current_key = key
        current_value = value
        end = 1

if end == 1:
    print '%s\t%s' % (key, value)

#!/usr/bin/python

import sys
import os
import csv

filepath = os.environ['mapreduce_map_input_file']
filename = os.path.split(filepath)[-1]

f = csv.reader(sys.stdin)
for line in f:
    if "parking" in filename:
        date = line[1].split('-')
        weekend = ['05','06','12','13','19','20','26','27']
        if date[2] in weekend:
            print '%s\t%s' % (line[2], 1)
        else:
            print '%s\t%s' % (line[2], 0)

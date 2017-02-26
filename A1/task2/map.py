#!/usr/bin/python

import sys
import os
import csv

filepath = os.environ['mapreduce_map_input_file']
filename = os.path.split(filepath)[-1]

f = csv.reader(sys.stdin)
for line in f:
    if "parking" in filename:       
        print '%s\t%s' % (line[2], 1)

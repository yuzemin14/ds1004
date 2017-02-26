#!/usr/bin/python

import sys
import os
import csv

filepath = os.environ['mapreduce_map_input_file']
filename = os.path.split(filepath)[-1]

f = csv.reader(sys.stdin)
for line in f:
    if "parking" in filename:
        value = ', '.join((line[14],line[6],line[2],line[1]))      
        print '%s\t%s' % (line[0],value)
    if "open" in filename:
        print '%s\t%s' % (line[0],'open')

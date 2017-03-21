from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

def weekend(x):
    date = x[1].split('-')
    weekend = ['05','06','12','13','19','20','26','27']
    if date[2] in weekend:
        return (1, 0)
    else:
        return (0, 1)

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x))    
    counts = lines.map(lambda x: (x[2], weekend(x))) \
                  .reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
    counts = counts.map(lambda x: "%s\t%0.2f, %0.2f" %(x[0], x[1][0]/8.0, x[1][1]/23.0))
    counts.saveAsTextFile("task7.out")

    sc.stop()

from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x))    
    counts = lines.map(lambda x: (x[2], (float(x[12]), 1))) \
                  .reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
    counts = counts.map(lambda x: "%s\t%0.2f, %0.2f" %(x[0], x[1][0], x[1][0]/x[1][1]))
    counts.saveAsTextFile("task3.out")

    sc.stop()

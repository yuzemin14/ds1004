from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

def unpaid(x):
    if len(x) > 20:
        return ', '.join((x[14],x[6],x[2],x[1]))
    else:
        return 'o'

if __name__ == "__main__":
    sc = SparkContext()
    rdd1 = sc.textFile(sys.argv[1], 1)
    rdd2 = sc.textFile(sys.argv[2], 1)
    lines = sc.union([rdd1, rdd2])
    lines = lines.mapPartitions(lambda x: reader(x))    
    counts = lines.map(lambda x: (x[0], unpaid(x))) \
                  .groupByKey() \
                  .filter(lambda x: len(x[1]) == 1) \
                  .mapValues(list)
    counts = counts.map(lambda x: (x[0], ''.join(x[1]))) \
                   .filter(lambda x: len(x[1]) > 1)
    counts = counts.map(lambda x: "%s\t%s" %(x[0], x[1]))
    counts.saveAsTextFile("task1.out")

    sc.stop()

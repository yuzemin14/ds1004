from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

def plate_state(x):
    return ', '.join((x[14],x[16]))

if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x))    
    counts = lines.map(lambda x: (plate_state(x), 1)) \
                  .reduceByKey(add) \
                  .sortBy(lambda x: x[1], False)
    counts = sc.parallelize(counts.take(20))
    counts = counts.map(lambda x: "%s\t%s" %(x[0],x[1]))
    counts.saveAsTextFile("task6.out")

    sc.stop()

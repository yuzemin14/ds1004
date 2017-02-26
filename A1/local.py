import os
import csv
os.chdir("C:/NYU/2017Spring/DS1004/Lab/A1/data")

lis1 = []
with open("parking-violations.csv") as f:
    f = csv.reader(f)
    for line in f:
        value = ', '.join((line[14],line[6],line[2],line[1]))
        lis1.append([line[0],value])

lis2 = []
with open("open-violations.csv") as f:
    f = csv.reader(f)
    for line in f:
        lis2.append([line[0], 'open'])

lis = lis1 + lis2
list_sorted = sorted(lis, key=lambda l:l[0])

current_key = None

for line in list_sorted[0:300]:
    end = 0
    key, value = line[0], line[1]
    
    if current_key == None:
        current_key = key
        current_value = value
        end = 1
    elif current_key == key:
        current_key = None
        current_value = None
    else:
        print ('%s\t%s' % (current_key, current_value))
        current_key = key
        current_value = value
        end = 1
        
if end == 1:
    print ('%s\t%s' % (key, value))
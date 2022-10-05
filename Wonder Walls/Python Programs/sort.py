import operator
import csv
sample = open("Competitor Details.csv","r")
csv1 = csv.reader(sample,delimiter=',')
sort = sorted(csv1,key=operator.itemgetter(10))
for eachline in sort:
    print (eachline)


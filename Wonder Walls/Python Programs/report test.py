import csv
myList = []
with open("Customer Details.csv", "rt") as csvFile:
    csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
    for line in csvReader:
        myList.append(line)
        
    for item in myList:
        print(item)


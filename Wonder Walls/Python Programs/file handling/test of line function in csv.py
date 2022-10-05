import csv

with open("names.csv", "r") as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter=",")

    for line in csvReader:
        print(line["name"])
        print(line["number"])
        

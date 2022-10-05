import csv
with open("Customer Details.csv", "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for line in csvReader:
        print("Reaction Test 1")
    

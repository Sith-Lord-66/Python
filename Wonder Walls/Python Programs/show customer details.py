import csv

with open("Customer Details.csv", "rt") as csvFile:
    csvReader = csv.reader(csvFile, lineterminator = "\n", delimiter = ",")
    number = str(input("What is your asigned number? "))
    print(number)
    wwNumber = ("WW" + number)
    for row in csvReader:
        for field in row:
                if field == wwNumber:
                    print(row)


            
                

import csv

file = open("names.csv")
numline = len(file.readlines())
print (numline)

with open("names.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
            
    name = input("What is your full name?\n")
    number = input("What is your assigned number?\n")
    if name or number in csvReader:
        print("done")
        print(number)
        for line in csvReader:
            if :
                print(line[int(number)])
                break

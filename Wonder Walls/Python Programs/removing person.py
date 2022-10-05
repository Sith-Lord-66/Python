import csv

def find():
    saveLines = []
    file = open("Customer Details.csv", "r")
    text = file.read()
    length = len(open("Customer Details.csv").readlines())
    print(length)
    lines = open("Customer Details.csv", 'r').readlines()
    lines = text
    with open("Customer Details.csv", "rt") as csvFile:
        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
        for x, line in enumerate(csvFile):
            if x == int(number):
                saveLines.append("\n")
            else:
                x+1
                saveLines.append(line)
        out = open("Customer Details.csv", 'w')
        print(saveLines)
        out.writelines(saveLines)
        out.close()
        CustomerDetails = open("Customer Details.csv", "r")
        with open("Customer Details.csv", "r") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for line in csvReader:
                print(line)
                
with open("Customer Details.csv", "rt") as csvFile:
    csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
    firstName = str(input("What is your full name? "))
    lastName = str(input("What is your full name? "))
    number = str(input("What is your asigned number? "))
    print(number)
    for row in csvReader:
        if firstName and lastName and number in row:
            find()

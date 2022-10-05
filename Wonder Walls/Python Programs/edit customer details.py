import csv

def find():
    with open("Customer Details.csv", "rt") as csvFile:
        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
        firstName = str(input("What is your first name? "))
        lastName = str(input("What is your first name? "))
        number = str(input("What is your asigned number? "))
        print(number)
        for row in csvReader:
            if firstName in row:
                score = input(str("Please enter your score"))
                saveLines = []
                with open("Customer Details.csv", "rt") as csvFile:
                    csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
                    for x, line in enumerate(csvFile):
                        if x == int(number):
                            saveLines.append(line)
                            saveLines[-1] = saveLines[-1].strip()
                            saveLines.append("," + score + "\n")
                        else:
                            x + 1
                            saveLines.append(line)
                    print(saveLines)
                    out = open("Customer Details.csv", 'w')
                    out.writelines(saveLines)
                    out.close()
                    with open("Customer Details.csv", "r") as csvFile:
                        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
                        for line in csvReader:
                            print(line)
                    break

find()
                        

    

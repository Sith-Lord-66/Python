import csv
def checkNumb(function):
    
    with open("Customer Details.csv", "rt") as csvFile:
        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
        number = str(input("What is your asigned number? (Only the Number):"))
        wwNumber = ("WW" + number)
        for row in csvReader:
            for field in row:
                if field == wwNumber:
                    function()
def hi():
    print("hi")

def bye():
    print("bye")

z = input("write")
if z  == "1":
    checkNumb(print(row))
elif z == "2":
    checkNumb(hi)
elif z == "3":
    checkNumb(bye)

#Import Functions
import time
import subprocess
import csv
import random
import statistics
import operator

#Adding Customer
def AddCustomer():
    adding = True
    while (adding == True):
        file = open("Competitor Details.csv", "r")
        text = file.read()
        length = len(open("Competitor Details.csv").readlines())
        #reads line length to find number
        with open("Competitor Details.csv", "r") as csvFile:
            csvReader = csv.DictReader(csvFile)
            firstName = (input("To add a customer please enter their first name: "))
            checkName = False
            while checkName == False:
                for char in firstName:
                    if not char.isalpha():
                        print("not a valid entry, please enter a valid entry")
                        firstName = input("To add a customer please enter their firtst name: ")
                        checkName = False
                    else:
                        checkName = True
            lastName = input("Please enter their last name : ")
            checkLast = False
            while checkLast == False:
                for char in lastName:
                    if not char.isalpha():
                        print("not a valid entry, please enter an appropriate entry")
                        lastName = input("To add a customer please enter their last name: ")
                        checkLast = False
                    else:
                        checkLast = True
            customerNum = length
            postcode = input("Please enter their postcode: ")
            checkPost = False
            while checkPost == False:
                for char in postcode[0:2]:
                    if not char.isalpha():
                        print("not a valid entry, please enter an appropriate entry")
                        postcode = input("Please enter in their postcode: ")
                        checkPost = False
                if not postcode[2:5].isdigit():
                    print("not a valid entry, please enter an appropriate entry")
                    number = input("Please enter in their postcode: ")
                    checkPost = False
                for char in postcode[5:7]:
                    if not char.isalpha():
                        print("not a valid entry, please enter an appropriate entry")
                        postcode = input("Please enter in their postcode: ")
                        checkPost = False 
                    else:
                        checkPost = True
            gender = input("Please enter their Gender - M/F: ")
            checkGender = True
            while checkGender == True:
                if gender == "M":
                    checkGender = False
                elif gender == "F":
                    checkGender = False
                else:
                    gender = input("Please enter their Gender - M/F: ")
                    checkGender = True
            phoneNumber = input("Please enter in their phone number: ")
            checkNumber = True
            while checkNumber == True:
                for char in phoneNumber:
                    if not char.isalpha():
                        if len(phoneNumber) == 11:
                            checkNumber = False
                    else:
                        phoneNumber = input("Please enter in their phone number: ")
                        checkNumber = True
            email = input("Please enter their email address: ")
            checkEmail = True
            while checkEmail == True:
                if ".com" or ".co.uk" in email:
                    checkEmail = False
                else:
                    email = input("Please enter their email address: ")
                    checkEmail = True
            #asks user for a series of inputs which each have validation checks
            Details = {"First Name":firstName, "Last Name":lastName, "Number":("WW"+"%03d"%customerNum),"Postcode":postcode,"Gender":gender,"Phone Number":phoneNumber,"Email Address":email}
            with open("Competitor Details.csv", "a") as csvWrite:
                fieldnames = ["First Name","Last Name","Number","Postcode", "Gender", "Phone Number", "Email Address"]
                csvWriter = csv.DictWriter(csvWrite, lineterminator ="\n", fieldnames=fieldnames, delimiter = ",")
                csvWriter.writerow(Details)
                csvWrite.close()
                csvFile.close()
        #write into file all details and shows this to the user
        CustomerDetails = open('Competitor Details.csv', 'r')
        print("This is the customer you are trying to add:\n")
        print(CustomerDetails.readlines()[length])
        checkInput = input("Is this correct? Yes or No\n")
        #asks user if this information inputed is correct
        while (checkInput != ""): 
            if checkInput == "Yes":
                CustomerDetails.close()
                continues = input("Do you want to add another person? Yes or No\n")
                while (continues != ""):
                    if continues == "Yes":
                        adding = True
                    elif continues == "No":
                        adding = False
                        Functs()
                    else:
                        print("Not a valid entry")
                        continues = input("Do you want to add another person? Yes or No\n")
                #asks if you want to add another person
            elif checkInput == "No":
                lines = open("Competitor Details.csv", 'r').readlines()
                lines = text
                out = open("Competitor Details.csv", 'w')
                out.writelines(lines)
                out.close()
                CustomerDetails = open("Competitor Details.csv", "r")
                print(CustomerDetails.readlines())
            else:
                print("Not a valid entry")
                checkInput = input("Is this correct?\n")


def showFile():
    with open("Competitor Details.csv", "r") as csvFile:
        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
        for line in csvReader:
            print("\n")
            print(line)
            #shows the user all of the competitors in the file
            
    Functs()
                          
def reactionTest():
    finalScore1 = 0
    finalScore2 = 0
    finalScore3 = 0
    def test():
        plays = 0
        score1 = 0
        score2 = 0
        score3 = 0
        while plays <= 2:
            print("press enter when the word 'CLICK' appears:\n")
            time.sleep(random.randint(1,8))
            start = time.time()
            test = input("CLICK\n")
            end = time.time()
            total = end - start
            print("Your score was: " + '%.3f'%total)
            if plays == 0:
                score1 = total
            elif plays == 1:
                score2 = total
            elif plays == 2:
                score3 = total
            #times the user three times on inputing the correct value
            plays += 1
        print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
        aver = statistics.mean([score1,score2,score3])
        finalScore1 = str('%.3f'%aver)
        print("Your final score and average is:", finalScore1)
        #shows user their score before averaging and giving a final score
        plays = 0
        score1 = 0
        score2 = 0
        score3 = 0
        #resets variables
        correct = True
        while plays <= 2 and correct == True:
            print("press enter the number 66 when it appears on screen:\n")
            numbers = (random.randint(1,10))
            numb = 0
            while numb<numbers:
                time.sleep(random.randint(1,5))
                print(random.randint(1,65))
                numb += 1
            if numb >= numbers:
                time.sleep(random.randint(1,5))
                start = time.time()
                test = input("66\n")
                if test == "66":
                    end = time.time()
                    total = end - start
                    print("Your score was: " + '%.3f'%total)
                    plays += 1
                    if plays == 1:
                        score1 = total
                        correct = True
                    elif plays == 2:
                        score2 = total
                        correct = True
                    elif plays == 3:
                        score3 = total
                        correct = False
                    #times the user three times on inputing the correct value
                else:
                    print("that is not a correct entry the test will now repeat")
                    numb = 0
                    correct = True
        print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
        aver = statistics.mean([score1,score2,score3])
        finalScore2 = str('%.3f'%aver)
        print("Your final score and average is:", finalScore2)
        #shows user their score before averaging and giving a final score
        plays = 0
        score1 = 0
        score2 = 0
        score3 = 0
        #resets variables
        correct = True
        while plays <= 2 and correct == True:
            print("press enter when the letters 't i w w' when the word 'GO' appears:\n")
            time.sleep(random.randint(1,8))
            start = time.time()
            test = input("GO\n")
            if test == "t i w w":
                end = time.time()
                total = end - start
                print("Your score was: " + '%.3f'%total)
                if plays == 0:
                    score1 = total
                elif plays == 1:
                    score2 = total
                elif plays == 2:
                    score3 = total
                    correct = False
                plays += 1
                #times the user three times on inputing the correct value
            else:
                print("This is not a valid entry and the test will now be reapeated")
                correct = True
        print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
        aver = statistics.mean([score1,score2,score3])
        finalScore3 = str('%.3f'%aver)
        print("Your final score and average is:", finalScore3)
        #shows user their score before averaging and giving a final score
        Times = []
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for x, line in enumerate(csvFile):
                if x == int(number):
                    Times.append(line)
                    Times[-1] = Times[-1].strip()
                    Times.append("," + finalScore1 + "," + finalScore2 + "," + finalScore3 + "\n")
                    #writes the competitors details and then their reaction times to the file
                else:
                    x + 1
                    Times.append(line)
                    #writes all other competitor details to file as well
            out = open("Competitor Details.csv", 'w')
            out.writelines(Times)
            #writes the list to file
            out.close()
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for row in csvReader:
                for field in row:
                    if field == wwNumber:
                        print("\n")
                        print(row)
                        print("\nYour climb times have been successfully added: to add another set of times select Reaction Time Tests from the menu")
                        #prints the file with new details added to the end
            
        Functs()
            
    number = ""
    x = 0

    while not (number):
        number = str(input("What is your assigned number? (Only the Number not the letters):"))
        x = 0
        #asks user to input their ID number
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            wwNumber = ("WW00" + number)
            for row in csvReader:
                for field in row:
                    if field == wwNumber:
                        x+=1
                        test()
                        #if ID number found, the user is taken to the desired function
            if x == 0:
                print("Invalid Entry")
                number = ""
                #if ID number not found user is prompted to renter ID number
            
def createfile():
    with open("Competitor Details.csv", "a") as csvWrite:
    #file created called Competitor Details
        fieldnames = ["First Name","Last Name","Number","Postcode", "Gender", "Phone Number", "Email Address", "Eiffel Tower Climb", "SkyScraper Climb", "Slemish Climb", "Reaction Test 1", "Reaction Test 2", "Reaction Test 3"]
        csvWriter = csv.writer(csvWrite, lineterminator ="\n", delimiter = ",")
        csvWriter.writerow(fieldnames)
        #Fieldnames added to file
    print("The File has been successfully created.")
    Functs()

def showDetails():
    number = ""
    x = 0

    while not (number):
        number = str(input("What is your assigned number? (Only the Number not the letters):"))
        x = 0
        #user asked to input their ID number
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            wwNumber = ("WW00" + number)
            for row in csvReader:
                for field in row:
                    if field == wwNumber:
                        x+=1
                        print(row)
                        #when found the competitor by searching for ID number the program then displays the data found in this location
            if x == 0:
                print("Invalid Entry")
                number = ""

    Functs()

def climb():
    climb = ""
    def editFile():
        Times = []
        climb = str(input("Please Enter your score for your completed Eiffel Tower climb: "))
        climb2 = str(input("Please Enter your score for your completed Skyscraper climb: ")) 
        climb3 = str(input("Please Enter your score for your completed Slemish climb: "))
        #user asked to input their climb scores
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for x, line in enumerate(csvFile):
                if x == int(number):
                    Times.append(line)
                    Times[-1] = Times[-1].strip()
                    Times.append("," + climb + ","  + climb2 + "," + climb3 +  "\n")
                    #their climb scores are then added to a list containing their other data
                else:
                    x + 1
                    Times.append(line)
                    #other competitor data also added
            out = open("Competitor Details.csv", 'w')
            out.writelines(Times)
            #this new list is written to the file
            out.close()
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for row in csvReader:
                for field in row:
                    if field == wwNumber:
                        print("\n")
                        print(row)
                        print("\nYour climb times have been successfully added")
        Functs()
    number = ""
    x = 0

    while not (number):
        number = str(input("What is your assigned number? (Only the Number not the letters):"))
        x = 0
        #asks user to input their ID number
        with open("Competitor Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            wwNumber = ("WW00" + number)
            for row in csvReader:
                for field in row:
                    if field == wwNumber:
                        x+=1
                        editFile()
                    #when ID number is found user is taken to the desired function
            if x == 0:
                print("Invalid Entry")
                number = ""
            #if not found user is prompted to renter data

def sortClimb():
    sample = open("Competitor Details.csv","r")
    csv1 = csv.reader(sample,delimiter=',')
    sort = sorted(csv1,key=operator.itemgetter(10), reverse = True)
    for eachline in sort:
        print("\n")
        print (eachline)
    Functs()
    #this sorts all competitors based on first climb time

def sortReaction():
    sample = open("Competitor Details.csv","r")
    csv1 = csv.reader(sample,delimiter=',')
    sort = sorted(csv1,key=operator.itemgetter(7), reverse = True)
    for eachline in sort:
        print("\n")
        print (eachline)
    Functs()
    #this sorts all competitors based on first reaction test

def shutDown():
        print("Shutting down...")
        time.sleep(5)
        raise SystemExit
        #shuts system down
    
def Log():
        print("\nLogging off...")
        time.sleep(5)
        print("\n--------------------------------------------------------------------------------\n\n")
        login()
        #returns user back to log on screen

def report():
    #report menu
    reportType = ""
    print("\nPlease Select a report type:\n1: Show An individual's Details\n2: Show all competitor Details\n3: Leader Board of First Reaction Time\n4: Leader Board of First Reaction Time Test\n5:Return to menu system")
    while (not reportType):
        reportType = input("\nReport Type: ")
        #asks user for input of desired report
        if reportType == "1":
            showDetails()
        if reportType == "2":
            showFile()
        if reportType == "3":
            sortReaction()
        if reportType == "4":
            sortClimb()
        if reportType == "5":
            Functs()
        else:
            reportType = ""
        #checks to find the input from list of reports


def Functs():
        chose = ""
        print ("\n\nPlease Select a function:\n\n1: Log Off\n2: Create Competitor Details File\n3: Add Customer\n4: Complete A Reaction Test \n5: Fill in Climb Scores\n6: Produce A Report\n\nPlease note in order to correctly run the system:\n1. First use create a file feature before adding competitor\n2. Then add any number of competitors\n3. Reaction tests must be after before entering climb times\n4. Reaction times can only be correctly entered after the Climb times for that competitor have been entered.")
        #prints function menu
        while (not chose):
                chose = input("\nFunction: ")
                if chose == "1":
                    Log()
                elif chose == "2":
                    createfile()
                elif chose == "3":
                    AddCustomer()
                elif chose == "4":
                    reactionTest()
                elif chose == "5":
                    climb()
                elif chose == "6":
                    report()
                else:
                    chose = ""
                #checks to see what function the user has selected


                    
                        
#Logging in system
def login():
        passCorrect = True
        exitLog = ""
        while (not exitLog):
            exitLog = input("Do you want to either:\n1:login\n2:shut down\n")
            if exitLog == "1":
                passCorrect = False
            elif exitLog == "2":
                shutDown()
            else:
                exitLog = ""
                
        username = ""
        password = ""
        trys = 0
        trysRemaining = 3
        passWrong = False
        while (trys <= 3 and passCorrect == False and passWrong == False):
            while (not username):
                username = input("Username: ")
                
            while (not password):
                password = input("Password: ")
            #asks user for input of username and password
            if trys <= 3 and username == "WonderWalls" and password == "Admin1":
                print("Welcome Wonder Walls Staff")
                passCorrect = True
                Functs()
                #if input is correct the function menu is loaded
            elif trys == 2 and trysRemaining == 1:
                print("You have entered your username or password incorrectly too many times. \nYour Account Has Been Locked.")
                passWrong = True
                print("Shutting down System")
                time.sleep(5)
                raise SystemExit
                #if input incorrect more than 3 times program is ended
            elif trys < 2 and trysRemaining > 1:
                trys += 1
                trysRemaining -= 1
                print ("That Username or Password is incorrect. You have ",trysRemaining, "try(s) remaining")
                username = ""
                password = ""
                #asks for user to reinput if incorrect
                
#-------------------------------------------------------------------------------------------------
#Start of Program
print("""
 _    _                 _             _    _       _ _     
| |  | |               | |           | |  | |     | | |    
| |  | | ___  _ __   __| | ___ _ __  | |  | | __ _| | |___ 
| |/\| |/ _ \| '_ \ / _` |/ _ \ '__| | |/\| |/ _` | | / __|
\  /\  / (_) | | | | (_| |  __/ |    \  /\  / (_| | | \__ \ 
 \/  \/ \___/|_| |_|\__,_|\___|_|     \/  \/ \__,_|_|_|___/
                                                           
--------------------------------------------------------------------------------""")


login()


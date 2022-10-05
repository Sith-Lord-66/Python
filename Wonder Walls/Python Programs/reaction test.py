import csv
import random
import time
import statistics

def reactionTest():
    finalScore = 0
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
            plays += 1
        print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
        aver = statistics.mean([score1,score2,score3])
        finalScore = str('%.3f'%aver)
        print("Your final score and average is:", finalScore)
        print (finalScore)
        saveLines = []
        with open("Customer Details.csv", "rt") as csvFile:
            csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
            for x, line in enumerate(csvFile):
                if x == int(number):
                    saveLines.append(line)
                    saveLines[-1] = saveLines[-1].strip()
                    saveLines.append("," + finalScore + "\n")
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
            print("Send to home")



        
                
    with open("Customer Details.csv", "rt") as csvFile:
        csvReader = csv.reader(csvFile, lineterminator ="\n", delimiter = ",")
        number = str(input("What is your asigned number? (Only the Number):"))
        wwNumber = ("WW" + number)
        for row in csvReader:
            for field in row:
                if field == wwNumber:
                    test()

reactionTest()


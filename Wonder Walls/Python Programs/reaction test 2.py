import random
import time

plays = 0
score1 = 0
score2 = 0
score3 = 0
while plays <= 2:
    correct = True
    print("press enter when the number 66 when it appears appears:\n")
    numbers = (random.randint(1,10))
    numb = 0
    while correct == True:
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
                if plays == 0:
                    score1 = total
                elif plays == 1:
                    score2 = total
                elif plays == 2:
                    score3 = total
                plays += 1
                correct = False
            else:
                print("that is not a correct entry the test will now repeat")
                numb = 0
                correct = True
print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
aver = statistics.mean([score1,score2,score3])
finalScore2 = str('%.3f'%aver)
print("Your final score and average is:", finalScore2)

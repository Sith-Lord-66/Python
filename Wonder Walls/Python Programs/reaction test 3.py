import time
import random

plays = 0
score1 = 0
score2 = 0
score3 = 0
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
    else:
        print("This is not a valid entry and the test will now be reapeated")
        correct = True
print("Your three scores are:" ,"\n",('%.3f'%score1),"\n",('%.3f'%score2),"\n",('%.3f'%score3))
aver = statistics.mean([score1,score2,score3])
finalScore1 = str('%.3f'%aver)
print("Your final score and average is:", finalScore3)

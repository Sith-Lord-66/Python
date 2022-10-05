import time
import random

        while plays !=> 4:
        print("press enter when the word 'CLICK' appears:\n"
        time.sleep(random.randint(1,8))
        start = time.time()
        test = input("CLICK\n")
        end = time.time()
        total = end - start
        print (" Your score was: " + '%.3f'%total)
        plays + 1
        

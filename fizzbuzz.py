
# ============================================
#      The popular 'FizzBuzz' function.
# --------------------------------------------
# The function accepts INTEGER n as parameter.
# ============================================

import math
import os
import random
import re
import sys

def fizzBuzz(n):
    
    # Constraints
    if n > 0 and n < (2*(10**5)):
        # Loop from 1 to n
        for fb in range(1,n):
            if(fb % 3 == 0 and fb % 5 ==0):
                print('FizzBuzz')
            elif(fb % 3 == 0):
                print('Fizz')
            elif(fb % 5 == 0):
                print('Buzz')
            else:
                print(fb)
    else:
        print("Please, inform a number between 1 and 2x10**5")
    print("That's it!")
    

if __name__ == '__main__':

    print("Please, inform a number between 1 and 2x10**5")

    n = int(input())

    fizzBuzz(n)

# Name: Leah Balhous
# Title: Random Number Average
# Date: March 24th, 2025
# Description: This program gets the average of 100 random numbers

import random

numbers = []
for i in range(100) :
    num = random.randint(0, 100)
    numbers.append(num)
print(sum(numbers)/100)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 0):
    last_digit = number % 10
else:
    last_digit = -(-number % 10)

if (last_digit == 0):
    compl = "and is 0"
elif (last_digit <= 5):
    compl = "and is less than 6 and not 0"
else:
    compl = "and is greater than 5"

msm = "Last digit of " + str(number) + " is " + str(last_digit) + " " + compl
print(msm)

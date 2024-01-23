#!/usr/bin/python3
import random
number = random.randint(-10, 10)
new_number = number
if number > 0:
    number = 0
    print(new_number, "is positive")
elif number < 0:
    print(new_number, "is zero")
else:
    print(new_number,"is negative")

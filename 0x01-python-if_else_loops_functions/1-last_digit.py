#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number
last_digit = new_number % 10
if last_digit > 5:
    last_digit =0
    print(f"last digit of {new_number} is {last_digit} and is greater than 5")
elif last_digit < 6:
    print(f"last digit of {new_number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"last_digit of {new_number} is {last_digit} and is 0")
    
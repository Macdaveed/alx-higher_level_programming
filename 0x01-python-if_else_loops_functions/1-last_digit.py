#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = number
last_digit = abs(new_number) % 10
sign = '-' if new_number < 0 else ''
if last_digit > 5:
    print(f"last digit of {new_number} is {sign}{last_digit} and is greater than 5")
elif last_digit < 6:
    print(f"last digit of {new_number} is {sign}{last_digit} and is less than 6 and not 0")
else:
    print(f"last_digit of {new_number} is {sign}{last_digit} and is 0")
    
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = number
last_num = abs(new) % 10
sign = '-' if new < 0 else ''
literal = "and is than 6 and not 0"
new_literal = literal
if last_num > 5:
    print(f"last digit of {new} is {sign}{last_num} and is greater than 5")
elif last_num < 6:
    print(f"last digit of {new} is {sign}{last_num} and is less than 6 not 0")
else:
    print(f"last_digit of {new} is {sign}{last_num} and is 0")

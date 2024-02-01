#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = number
last_num = abs(new) % 10
sign = '-' if new < 0 else ''
output_string = f"Last digit of {new} is {sign}{last_num} and"
if last_num > 5:
    print(f"{output_string} is greater than 5")
elif last_num == 0:
    print(f"{output_string} is 0")
elif 0 < last_num < 6:
    print(f"{output_string} is less than 6 and not 0")
else:
    print()

#!/usr/bin/python3
import random

number = random.randint(-10, 10)
# YOUR CODE HERE
number_type = ""
if number > 0:
    number_type = "positive"
elif number == 0:
    number_type = "zero"
else:
    number_type = "negative"

print("{:d} is {:s}\n".format(number, number_type))

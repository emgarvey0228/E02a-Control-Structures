#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
    # On line 9, this fixes the problem of answering Red in various forms of capitalization (such as RED, rED, ReD)
    # If a space is added before or after the input, the new output is "Sorry, try again."
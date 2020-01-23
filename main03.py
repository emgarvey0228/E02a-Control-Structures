#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')
    # If the input color is red then the response would be correct
    # Lines 9-12 is a guessing game 
    # Lines 10 and 12 are indented because they represent a response
    # If the R in red is not capitalized, then the guess would be incorrect and the response is "Sorry, try again."
    # This tells me that color is tricky and if not spelled correctly or if it has a different capitalization, then the input would be incorrect

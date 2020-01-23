#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
    # This looks different from Main3 because now you have the input option of spelling Red like red
    # This is going to help solve the issue of having the output tell the user that their input is incorrect when it is correct, just has a slightly different variable
    # I spelled "rED" into the terminal and the response was "Sorry, try again."
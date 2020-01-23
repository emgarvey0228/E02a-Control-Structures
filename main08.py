#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')
        # Lines 10-17 are indented to show that this is the same command/ response to the first question
        # If line 10 was put before line 9, the question would not appear and "color = color.lower().strip()" would
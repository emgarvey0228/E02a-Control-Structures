#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.')
    # Main7 now has added lines
    # The new lines now help the user guess the color correctly by adding in hints (only if the guess is close enough to red- AKA pink)
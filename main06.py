#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')
    # Line 9 now has .strip() added
    # The only way I found that ruined the logic of line 9 is if you spell red with spaces inbetween the letters such as "r e d"
#!/usr/bin/env python
#
# This is a simple python script which outputs the table of number inputed.
# License: MIT License
#

import sys

try:
    num = sys.argv[1]
except IndexError:
    num = input("Enter the number you want the table of: ")

while True:
    try:
        num = int(num)
        break
    except ValueError:
        num = input("Enter the number you want the table of: ")

for i in range(1,11):
    answer = num * i
    message = "{} x {} = {}".format(num,i,answer)
    print(message)

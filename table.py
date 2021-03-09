#!/usr/bin/env python
#
# This is a simple python script which outputs the table of number inputed.
# License: MIT License
#

import sys

def getNum():
    try:
        num = sys.argv[1]
    except IndexError:
        num = input("Enter the number you want the table of: ")
    return num

def validateNum(num):
    try:
        num = int(num)
    except ValueError:
        print("Invalid Number",file=sys.stderr)
        exit(1)
    return num

def PrintTable(num):
    for i in range(1,11):
        answer = num * i
        table = "{} x {} = {}".format(num,i,answer)
        print(table)

def main():
    num = validateNum(getNum())
    PrintTable(num)

if __name__ == "__main__":
    main()

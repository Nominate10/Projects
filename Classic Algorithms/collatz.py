#!/usr/bin/env python3

##Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process:
##If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

def isEven(n):
    return n % 2 == 0

# n > 1
n = int(input("Enter a number: "))
steps = []

if n <= 1:
    print("Please use a number greater than 1")
else:
    while n != 1:
        if isEven(n):
            n = n/2
        else:
            n = (n*3)+1
        steps.append(int(n))

    print("Number of steps: ", len(steps))
    print("This is your path: ", steps)

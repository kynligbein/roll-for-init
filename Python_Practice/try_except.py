#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:17:44 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

try:
    value = 10/0    
    number = int(input("Enter a number: "))
    print(number)
# This first exception error catches the specific error, divide by zero
# in this case, and prints the actual error.
except ZeroDivisionError as err:
    print(err)
# This second exception looks for the invalid input error and uses the 
# error message stipulated by the programmer (me)
except ValueError:
        print("Invalid Input")
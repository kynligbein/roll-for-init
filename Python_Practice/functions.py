#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:56:18 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

def sayHi(name, age):
    print("Hello " + name + ", you are " + age)


sayHi("Bob", "35")
sayHi("John", "65")

#Using this file for the Return Statement section of tutorial

def cube(num):
    return num*num*num
#nothing entered after the 'return' in a function gets processed

result = cube(4)
print(result)
    
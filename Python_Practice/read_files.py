#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:32:40 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

# Variations to opening the file are "r" for read, "w" for write, "a" for append
# and "r+" for read & write.

ef = open("crew.txt", "r")
print("The filename is: ", ef.name)
# .readable() checks to make sure if the file readable
print("The file is readable: ", ef.readable())
for crew in ef.readlines():
    print(crew)
ef.close()

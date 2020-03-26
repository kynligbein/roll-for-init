#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:52:05 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

# Section in tutorial covering 2D Lists and Nested Loops

# Using a list of lists to make a 2D grid
number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]       
]

#print(number_grid[2][1]) # Printing a specific section of the "grid"

for row in number_grid:
    for col in row:
        print(col)
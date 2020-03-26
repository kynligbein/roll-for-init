#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:18:48 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

class Student:
    
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

# Function added in later section of Tutorial to showcase how functions work 
# in modules and classes.
        
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
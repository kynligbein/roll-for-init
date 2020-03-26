#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:53:32 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

from Student import Student

student1 = Student("Lenore", "Growling", 3.8, False)
student2 = Student("Emma", "Borking", 3.5, False)

print(student1.on_honor_roll())

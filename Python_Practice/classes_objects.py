#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:07:24 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.

This section of the tutorial covers objects which was also covered 
during a "peer teaching" section of my Python 2 class. 

@author: kynligbein
"""

from Student import Student

student1 = Student("Jason", "Data Analytics", 3.0, False)
student2 = Student("Noelle", "Art", 4.0, False)

print(student2.gpa)

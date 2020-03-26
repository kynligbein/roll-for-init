#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:21:11 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein

Originally just copy & pasted the functions from the Chef.py class and then 
modified the functions to reflect the new cuisine for the new class.

instead of copy/pasting from other class, do the following:
"""
from Chef import Chef

class ChineseChef(Chef):
# copied and modified this function to overwrite it for the new chef cuisine/class
    def make_special_dish(self):
        print("The chef makes crispy duck")

    def make_fried_rice(self):
        print("The chef makes fried rice")
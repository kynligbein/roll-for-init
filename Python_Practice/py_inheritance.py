#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:13:52 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.

related to Objects and Modules, this shows how one class can inherit
elements from another class

@author: kynligbein
"""

from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_special_dish()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
myChineseChef.make_chicken()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:53:42 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""

monthConversions = {"Jan": "January",
                    "Feb": "February",
                    "Mar": "March",
                    "Apr": "April",
                    "May": "May",
                    "Jun": "June",
                    "Jul": "July",
                    "Aug": "August",
                    "Sep": "September",
                    "Oct": "October",
                    "Nov": "November",
                    "Dec": "December",
                    }
#print(monthConversions) #prints the whole dictionary
#print(monthConversions("Dec")) #prints specific key

print(monthConversions.get("Luv")) #using get() method avoids returning an 
#error if an invalid key is entered by returning "none" if no key is found

print(monthConversions.get("Luv", "Not a valid key"))  #using the get() method
#to includ an actual message  instead of just 'none'.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:30:40 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""
# =============================================================================
# This is version 2 of the tutorial's guessing game script.
# I added the .lower() as described below and created a list of words to make
# the secret word random every time the game is played.
# =============================================================================

import random

secretList = ["giraffe", "lion", "bear", "monkey", "otter"]
secretWord = random.choice(secretList)
guess = ""
guessCount = 0
guessLimit = 3
out_of_guesses = False

print(secretWord) 
while guess != secretWord and not(out_of_guesses):
    if guessCount < guessLimit:
        guess = input("Enter guess: ").lower() #not in tutorial, added to allow 
        #for if user enters caps because otherwise the right word would show as
        #wrong. "Giraffe" would be wrong without .lower()
        guessCount += 1
    else:
        out_of_guesses = True

   
if out_of_guesses:
    print("You have run out of guesses, you lose!")
else:
    print("You guessed the secret word, you win!")
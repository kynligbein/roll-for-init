#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:32:15 2020
Following the "giraffe academy" freecodecamp.org python tutorial. 
These are attempts to get better and more knowledgeable
about python for class.

Tutorial uses PyCharm to code, I am using Spyder.
@author: kynligbein
"""
from Question import Question

question_prompts = [
        "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
        "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Gross\n\n"
]

questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b"),
]

def run_quiz(questions):
    score = 0
    for Question in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct!")
    
run_quiz(questions)

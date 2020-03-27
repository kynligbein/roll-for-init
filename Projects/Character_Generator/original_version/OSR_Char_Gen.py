#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Incredibly basic random character generator to start for final project.
Using very basic randomizing from lists for this draft with no functions as yet.
Final project will include a choice between a randomly generated name or choosing
a name for the character as well as choosing skills.

Please be aware this is extremely basic to lay groundwork code only. 

"""
import random

#create lists to generate random names - temporary
vowel = ['a','e','i','o','u']
alphabet = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

print()
print("Random character generator for the Bloody Basic Weird Fantasy RPG")
print()

#Randomly generate stats and identity.
class1 = ["Magus\n","Puissant\n","Thief\n","Idolator\n","Woodwose\n"]
class2 = random.choice(class1)
race1 = ["Human\n","Elf\n","Grotesques\n","Satyr\n","Dwarf\n"]
race2 = random.choice(race1)
gender1 = ["Female\n","Male\n","Non-Binary\n"]
gender2 = random.choice(gender1)
strength = random.randint(3,18)
dexterity = random.randint(3,18)
constitution = random.randint(3,18)
intelligence = random.randint(3,18)
wisdom = random.randint(3,18)
charisma = random.randint(3,18)

#Name builder
n1 = random.choice(alphabet).upper()
n2 = random.choice(vowel)
n3 = random.choice(alphabet)
n4 = random.choice(alphabet)
n5 = random.choice(vowel)
n6 = random.choice(alphabet)

#Print and write everything
name = (n1+n2+n3+n4+n5+n6)
print("Name:",name)
print("Class:",class2,"Gender:",gender2,"Race:",race2,"STR:",strength,"DEX:",\
      dexterity,"CON:",constitution,"INT:",intelligence,"WIS:",wisdom,"CHA:",\
      charisma)


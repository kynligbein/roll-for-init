#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:12:41 2020

Bloody Basic: Weird Fantasy RPG Random Character Generator
Version 1.2.0

Initial version of this program was for a Python 1 class.
This program completely generates a randomized character at first level using
the rules as provided by the Bloody Basic: Weird Fantasy rpg.
The class of "Wodwose" is a home-ruled class added to include a "weird fantasy"
version of the druid class.

@author: kynligbein
"""

import random
import string

rand_race = ()
rand_class = ()
rand_name = ()
specAbil = ()
stats = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}

def rollStats():
    stats['STR'] = random.randint(3,18)
    stats['DEX'] = random.randint(3,18)
    stats['CON'] = random.randint(3,18)
    stats['INT'] = random.randint(3,18)
    stats['WIS'] = random.randint(3,18)
    stats['CHA'] = random.randint(3,18)
#    print(stats)

def pc_name():
    global rand_name
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    n1 = random.choice(consonants)
    n2 = random.choice(vowels)
    n3 = random.choice(consonants)
    n4 = random.choice(consonants)
    n5 = random.choice(vowels)
    n6 = random.choice(consonants)
    name = (n1+n2+n3+n4+n5+n6)
    rand_name = name.title()
#    print(rand_name)

def classes():
    global rand_class
    with open("library/classes.txt") as f:
        lines = f.readlines()
        char_class = random.choice(lines)
        rand_class = char_class
#        print(rand_class)

def races():
    global rand_race
    with open("library/races.txt") as f:
        lines = f.readlines()
        char_race = random.choice(lines)
        rand_race = char_race
#        print(rand_race)

def raceMod():
    global specAbil
    if 'Elf' in rand_race:
        stats['DEX'] += 1
        stats['CON'] -= 1
        with open("library/elf.txt") as sa:
            text = sa.read()
            specAbil = text
    elif 'Dwarf' in rand_race:
        stats['CON'] += 1
        stats['CHA'] -= 1
        with open("library/dwarf.txt") as sa:
            text = sa.read()
            specAbil = text
    elif 'Grotesque' in rand_race:
        stats['STR'] += 1
        stats['CHA'] -= 1
        with open("library/grotesque.txt") as sa:
            text = sa.read()
            specAbil = text
    elif 'Satyr' in rand_race:
        stats['CON'] += 1
        stats['WIS'] -= 1
        with open("library/satyr.txt") as sa:
            text = sa.read()
            specAbil = text
    else:
        with open("library/human.txt") as sa:
            text = sa.read()
            specAbil = text
    for k, v in stats.items(): print(k, ":", v, end = " ")
    
def hpSave():
    if 'Magus' in rand_class:
        _HP_ = random.randint(1,4)
        saves = ("Fortitude: 15 Reflexes: 15 Will: 13")
    elif 'Idolator' in rand_class:
        _HP_ = random.randint(1,6)
        saves = ("Fortitude: 13 Reflexes: 15 Will: 13")
    elif 'Thief' in rand_class:
        _HP_ = random.randint(1,6)
        saves = ("Fortitude: 15 Reflexes: 13 Will: 15")
    elif 'Puissant' in rand_class:
        _HP_ = random.randint(1,8)
        saves = ("Fortitude: 13 Reflexes: 15 Will: 15")
    elif 'Wodewose' in rand_class:
        _HP_ = random.randint(1,6)
        saves = ("Fortitude: 15 Reflexes: 15 Will: 13")
    print("\n","HP:", _HP_, saves, "\n")

def classMod():
    if 'Magus' in rand_class:
        with open("library/magusAbil.txt") as f:
                classAbil = f.read()
                print(classAbil)
        with open("library/cantrap.txt") as f:
            cantrap = f.readlines()
            grimoire = random.choices(cantrap, k = 3)
        print("Grimoire:", grimoire)
    elif 'Idolator' in rand_class:
        with open("library/clericAbil.txt") as f:
                classAbil = f.read()
                print(classAbil)
        with open("library/taboo.txt") as f:
            taboo = f.readlines()
            vow = random.choices(taboo, k = 3)
        with open("library/orison.txt") as f:
            orison = f.readlines()
            bless = random.choices(orison, k = 3)
        print("Granted Orisons:", bless, "\n", "Taboos:", vow)
    elif 'Wodewose' in rand_class:
        with open("library/druidAbil.txt") as f:
                classAbil = f.read()
                print(classAbil)
        with open("library/ritual.txt") as f:
            ritual = f.readlines()
            rites = random.choices(ritual, k = 3)
        with open("library/shape.txt") as f:
            shape = f.readlines()
            wild = random.choice(shape)
        print("Known Rituals:", rites, "\n", "Wild Shape:", wild)
    elif 'Puissant' in rand_class:
        with open("library/fightAbil.txt") as f:
                classAbil = f.read()
                print(classAbil)
        with open("library/feats.txt") as f:
            feats = f.readlines()
            fight = random.choices(feats, k = 3)
        print("Feats of Combat Excellence:", fight)  
    else:
        thiefMod()

def thiefMod():
    if 'Thief' in rand_class:
        with open("library/thiefAbil.txt") as f:
                classAbil = f.read()
                print(classAbil)
        if stats['CHA'] >= 13 and stats['DEX'] >= 13:
            with open("library/odal.txt") as f:
                subclass = f.read()
                print(subclass)
        elif stats['CHA'] >= 15:
            with open("library/demi.txt") as f:
                subclass = f.read()
                print(subclass)
        else:
            print("Not able to take a sub-class.")
        
def newPC():
    rollStats(), pc_name(), races(), classes()
    print(rand_name, "the", rand_race.rstrip(), rand_class.rstrip())
    raceMod()
    hpSave()
    print(specAbil)
    classMod()
    goAgain()
        
def main():
    print()
    with open("library/intro.txt", "r") as f:
        f_contents = f.read()
        print(f_contents)
        
    anykey = input("Press any key to begin.\n")

    newPC()
    
def goAgain():
    again = input("Would you like to create another character? Y or N: ")
    if again == "Y":
        newPC()
    elif again == "N":
        print("Thank you for using this random character generator!")
        exit
    else:
        print("\nPlease enter either a 'Y' for yes or 'N' no.")
        goAgain()
main()


    
#print(rand_name, "the", rand_race, rand_class)

#testStatMod()

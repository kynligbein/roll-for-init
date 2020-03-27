#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:31:54 2019

@author: kynligbein
"""

import random

class1 = ["Magus\n","Puissant\n","Thief\n","Idolator\n","Woodwose\n"]
class2 = random.choice(class1)
race1 = ["Human","Elf","Grotesques","Satyr","Dwarf"]
race2 = random.choice(race1)

cantrap1 = ["Audible Glamer", "Color Spray", "Eldritch Bolts", "Hold Portal", \
            "Kalinoth's Abjuration", "Ken Gibberish", "Illuminate", "Prithian's Juvenile Lust", \
            "Read Magic", "Reveal Dweomers", "Sigil of Deflection", "Slumber"]

feats1 = ["Artfull Dodge", "Cleave", "Critical Hit", "Far Shot", "Fight Blind" \
          "Guards & Wards", "Iron Fist", "Power Attack", "Quick", "Shield Bash", \
          "Sword & Dagger", "Weapon Focus"]


strength = random.randint(3,18)
dexterity = random.randint(3,18)
constitution = random.randint(3,18)
intelligence = random.randint(3,18)
wisdom = random.randint(3,18)
charisma = random.randint(3,18)

def races():
    spec_abil = ()
    if race2 == "Human":
        spec_abil = ("May advance as far as possible in any class and are \
                     permitted to take any subclass in the game.\n")
    elif race2 == "Elf":
        spec_abil = ("See in the dark 60'. Automatically find any secret or \
                     hidden doors within 5' they pass. Immune to paralysis. \
                     Access to Heartspell regardless of class.\n")
        dexterity + 1
        constitution - 1
    elif race2 == "Grotesques":
        spec_abil = ("May cast the Orison 'Malison' once per day. +2 bonus on \
                     Saving Throws versus Fear.\n")
        strength + 1
        charisma - 1
    elif race2 == "Satyr":
        spec_abil = ("See in the dark 60'. Can use the horns on their heads \
                     to make a headbutt attack each round for 1d4 damage. +2 \
                     bonus on Saving Throws against the special abilities of \
                     magical beasts and the Fey.\n")
        constitution + 1
        wisdom - 1
    elif race2 == "Dwarf":
        spec_abil = ("None yet, but you're short.\n")
    else:
        print("How did you mess up what race you are?")
        
    print("Special Abilities: ",spec_abil)

def str_stat():
    str_mod = ()
    if strength in range (3,9):
        str_mod = ("Effete!")
    elif strength in range (9,13):
        str_mod = ("Average")
    elif strength in range (13,19):
        str_mod = ("Mighty!")
    else:
        print("Something is wrong with this stat!")
    
    print("STR:",strength,str_mod, end=" ")
    
    
def dex_stat():
    dex_mod = ()
    if dexterity in range (3,9):
        dex_mod = ("Oafish!")
    elif dexterity in range (9,13):
        dex_mod = ("Average")
    elif dexterity in range (13,19):
        dex_mod = ("Nimble!")
    else:
        print("Something is wrong with this stat!")
    
    print("DEX:",dexterity,dex_mod, end=" ")
    
def con_stat():
    con_mod = ()
    if constitution in range (3,9):
        con_mod = ("Oafish!")
    elif constitution in range (9,13):
        con_mod = ("Average")
    elif constitution in range (13,19):
        con_mod = ("Nimble!")
    else:
        print("Something is wrong with this stat!")
    
    print("CON:",constitution,con_mod)
    
def int_stat():
    int_mod = ()
    if intelligence in range (3,9):
        int_mod = ("Mooncalf!")
    elif intelligence in range (9,13):
        int_mod = ("Average")
    elif intelligence in range (13,19):
        int_mod = ("Canny!")
    else:
        print("Something is wrong with this stat!")
    
    print("INT:",intelligence,int_mod, end=" ")   
    
def wis_stat():
    wis_mod = ()
    if wisdom in range (3,9):
        wis_mod = ("Foolish!")
    elif wisdom in range (9,13):
        wis_mod = ("Average")
    elif wisdom in range (13,19):
        wis_mod = ("Sophic!")
    else:
        print("Something is wrong with this stat!")
    
    print("WIS:",wisdom,wis_mod, end=" ") 
    
def cha_stat():
    cha_mod = ()
    if charisma in range (3,9):
        cha_mod = ("Vile!")
    elif charisma in range (9,13):
        cha_mod = ("Average")
    elif charisma in range (13,19):
        cha_mod = ("Charming!")
    else:
        print("Something is wrong with this stat!")
    
    print("CHA:",charisma,cha_mod) 
    
def armor():
    if dexterity in range (3,9):
        AC = dexterity - 1
    elif dexterity in range (9,13):
        AC = dexterity
    elif dexterity in range (13,19):
        AC = dexterity + 1
    print("AC: ",AC, end=" ")
    
def hp_saves():
    if class2 == "Magus\n":
        health = random.randint(1,4)
    elif class2 == "Idolator\n":
        health = random.randint(1,6)
    elif class2 == "Thief\n":
        health = random.randint(1,6)
    elif class2 == "Puissant\n":
        health = random.randint(1,8)
    elif class2 == "Woodwose\n":
        health = random.randint(1,6)
    else:
        print("You get just 1 HP")
    print("HP: ",health,"\n")
    
def classes():
    class_abil = ()
    class_sp = ()
    if class2 == "Magus\n":
        if intelligence < 9:
            return class2
        else:
            class_abil = ("The Magus may cast Cantraps. They may only prepare \
                          cantraps they have learned and copied from their grimiores. \
                          Magi start with three first level spells in their grimiores.")
            cantrap2 = random.choices(cantrap1, k = 3)
            class_sp = ("Grimiore:",cantrap2)
            
    elif class2 == "Puissant\n":
        if strength < 9:
            return class2
        else:
            class_abil = ("Puissants can perform feats of combat excellence which \
                          can only performed a certain number of times per day \
                          per level - once per day at first level. They learn \
                          three at first level, then one per level after.")
            feats2 = random.choices(feats1, k = 3)
            class_sp = ("Feats of Combat Excellence:",feats2)
            
    elif class2 == "Thief\n":
        if dexterity < 9:
            return class2
        else:
            class_abil = ("Thieves may Backstab their opponents; surprise attacks \
                          from behind do double damage, as well as several specialized \
                          skills (see book for skills). Thieves also gain a subclass \
                          if they qualify for it.")

#   elif class2 == "Woodwose\n":
        

    print("class abilities:",class_abil,"\n",class_sp)            
            
#def hit_points():
    

print(race2, end=" ")
print(class2)

str_stat()
dex_stat()
con_stat()
int_stat()
wis_stat()
cha_stat()
armor()
hp_saves()
races()    
classes()


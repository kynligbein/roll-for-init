#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:24:16 2019

@author: kynligbein
"""

import random

class1 = ["Magus\n","Puissant\n","Thief\n","Idolator\n","Woodwose\n"]
class2 = random.choice(class1)

cantrap1 = ["Audible Glamer", "Color Spray", "Eldritch Bolts", "Hold Portal", \
            "Kalinoth's Abjuration", "Ken Gibberish", "Illuminate", "Prithian's \
            Juvenile Lust", "Read Magic", "Reveal Dweomers", "Sigil of \
            Deflection", "Slumber"]
feats1 = ["Artfull Dodge", "Cleave", "Critical Hit", "Far Shot", "Fight Blind" \
          "Guards & Wards", "Iron Fist", "Power Attack", "Quick", "Shield Bash", \
          "Sword & Dagger", "Weapon Focus"]


strength = random.randint(3,18)
dexterity = random.randint(3,18)
constitution = random.randint(3,18)
intelligence = random.randint(3,18)
wisdom = random.randint(3,18)
charisma = random.randint(3,18)

def classes():
    class_abil = ()
    class3 = class2
    if class3 == "Magus":
        if intelligence < 9:
            return class2
        else:
            class_abil = ("The Magus may cast Cantraps. They may only prepare \
                          cantraps they have learned and copied from their \
                          grimiores. Magi start with three first level spells \
                          in their grimiores.")
            cantrap2 = random.choices(cantrap1, k = 3)
            print("Class abilities: ",class_abil, "\n", \
                  "Grimiore: ",cantrap2)
            
            
    elif class3 == "Puissant":
        if strength < 9:
            return class2
        else:
            class_abil = ("Puissants can perform feats of combat excellence. \
                          These can only performed a certain number of times \
                          per day per level - once per day at first level. They \
                          learn three at first level, then one per level after.")
            feats2 = random.choices(feats1, k = 3)
            print("class abilities: ",class_abil, "\n", \
                  "Feats of Combat Excellence: ",feats2)
            
    elif class3 == "Thief":
        if dexterity < 9:
            return class2
        else:
            class_abil = ("Thieves may Backstab their opponents; surprise attacks \
                          from behind do double damage, as well as several \
                          specialized skills (see book for skills). Thieves also \
                          gain a subclass if they qualify for it.")
            
            print("class abilities: ",class_abil, "\n")            
 
print(class2)
classes()           


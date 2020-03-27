#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final project for Jason Swart.
This program is a random character generator based on a tabletop roleplaying game
similar to the popular Dungeons & Dragons, but using rules for an OSR style game
called "Bloody Basic - Weird Fantasy Edition". (OSR is short for "Old School 
Renaissance" and is a style of game based on the original game rules from the 1970's
and early 1980's.) This program is designed to do the following:
    1. Using lists, randomly generate a series of variables relevant to the game.
    2. Use global variables to modify the output of others set in functions.
    3. Display the overall outut in a readable format for the user.
    4. Exit the program.
In full disclosure, the original plan was to include user choice between fully 
randomized character generation and some user input generation. Time and coding 
issues prevented that. It was intended to also have the program output the final
"character sheet" to a text file, but it resulted in the file showing "None" as
its only content and so was left off.
I was not present in class when students were paired into groups for discussion, 
but I have mutually discussed projects with Jill both in Python class and in our 
Data class.
"""
import random
#global variables set so functions can use the random list choice to affect local 
#variables.

class1 = ["Magus","Puissant","Thief","Idolator","Wodewose"]
class2 = random.choice(class1)

race1 = ["Human","Elf","Grotesque","Satyr","Dwarf"]
race2 = random.choice(race1)

strength = random.randint(3,18)
dexterity = random.randint(3,18)
constitution = random.randint(3,18)
intelligence = random.randint(3,18)
wisdom = random.randint(3,18)
charisma = random.randint(3,18)

#This function randomly generates a name from lists.
def pc_name():
    vowel = ['a','e','i','o','u']
    alphabet = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    n1 = random.choice(alphabet).upper()
    n2 = random.choice(vowel)
    n3 = random.choice(alphabet)
    n4 = random.choice(alphabet)
    n5 = random.choice(vowel)
    n6 = random.choice(alphabet)
    name = (n1+n2+n3+n4+n5+n6)
    print("\n",name, end = " the ")

#This next series of functions applies a modifier to a related global variable.
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
    
    print("CHA:",charisma,cha_mod, "\n")

#Similar to above functions, this function takes and modifies a global variable. 
def armor():
    if dexterity in range (3,9):
        AC = dexterity - 1
    elif dexterity in range (9,13):
        AC = dexterity
    elif dexterity in range (13,19):
        AC = dexterity + 1
    print("AC: ",AC, end=" ")

#This function also checks a random global variable and generates additional information
#to add to the final output based on the global variable.
def hp_saves():
    if class2 == "Magus":
        health = random.randint(1,4)
        saves = ("Fortitude: 15 Reflexes: 15 Will: 13")
    elif class2 == "Idolator":
        health = random.randint(1,6)
        saves = ("Fortitude: 13 Reflexes: 15 Will: 13")
    elif class2 == "Thief":
        health = random.randint(1,6)
        saves = ("Fortitude: 15 Reflexes: 13 Will: 15")
    elif class2 == "Puissant":
        health = random.randint(1,8)
        saves = ("Fortitude: 13 Reflexes: 15 Will: 15")
    elif class2 == "Wodewose":
        health = random.randint(1,6)
        saves = ("Fortitude: 15 Reflexes: 15 Will: 13")
    print("HP: ",health,saves,"\n")

#This function, like the others, takes a random global variable and adds to overall
#final output.
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
    elif race2 == "Grotesque":
        spec_abil = ("May cast the Orison 'Malison' once per day. +2 bonus on \
                     Saving Throws versus Fear.\n")
        strength + 1
        charisma - 1
    elif race2 == "Satyr":
        spec_abil = ("Can see in the dark up to 60'. Can use the horns on \
                     their heads to make a headbutt attack each round for 1d4 \
                     damage. +2 bonus on Saving Throws against the special abilities \
                     of magical beasts and the Fey.\n")
        constitution + 1
        wisdom - 1
    elif race2 == "Dwarf":
        spec_abil = ("Can see in the dark up to 60'. +3 bonus to saves versus \
                     poison and spells.\n")
        constitution + 1
        charisma - 1        
        
    print("Special Abilities:",spec_abil,)
#This is the same as the above function, but applies to a different variable.
def classes():
    class_abil = ()
    class_sp = ()
    cantrap1 = ["Audible Glamer", "Color Spray", "Eldritch Bolts", "Hold Portal", \
            "Kalinoth's Abjuration", "Ken Gibberish", "Illuminate", "Prithian's Juvenile Lust", \
            "Read Magic", "Reveal Dweomers", "Sigil of Deflection", "Slumber"]
    feats1 = ["Artfull Dodge", "Cleave", "Critical Hit", "Far Shot", "Fight Blind" \
          "Guards & Wards", "Iron Fist", "Power Attack", "Quick", "Shield Bash", \
          "Sword & Dagger", "Weapon Focus"]
    ritual1 = ["Bark Blast", "Burnt Offerings", "Cinder Shard", "Furry Pelt", \
               "Grow Horns", "Honey Bolt", "Iron Guts", "Root Bridge", "Sap Blood", \
               "Shoulder the Burden", "Smoke Signal", "Speak with Fungus", \
               "Tongue of Raven", "Water to Wine"]
    shape1 = ["Bear", "Wolf", "Fox", "Eagle", "Lion", "Hyena", "Vulture", "Gorilla"]
    taboo1 = ["Forswear any use of animals", "Forswear any contact with the opposite \
              sex", "Forswear speaking except when casting Orisons", "Forswear killing \
              with edged weapons", "Forswear the taking or holding of wealth", \
              "Forswear eating and drinking", "Forswear generosity", "Forswear mercy", \
              "Sacrifice all material wealth found that day", "Sacrifice the first \
              sentient being you come across with a sacrificial dagger"]
    orison1 = ["Bless", "Entangle", "Forfend", "Guidance", "Illuminate", "Malison" \
               "Mordacious Touch", "Purify Food & Drink", "Reveal Dweomers", \
               "Unctious Touch"]
    
    if class2 == "Magus":
        class_abil = ("The Magus may cast Cantraps. They may only prepare \
                      cantraps they have learned and copied from their \
                      grimiores. Magi start with three first level spells in \
                      their grimiores.")
        cantrap2 = random.choices(cantrap1, k = 3)
        class_sp = ("Grimiore:",cantrap2)
        
    if class2 == "Puissant":
        class_abil = ("Puissants can perform feats of combat excellence which \
                          can only performed a certain number of times per day \
                          per level - once per day at first level. They learn \
                          three at first level, then one per level after.")
        feats2 = random.choices(feats1, k = 3)
        class_sp = ("Feats of Combat Excellence:",feats2)
        
    if class2 == "Thief":
        class_abil = ("Thieves may Backstab their opponents; surprise attacks \
                      from behind do double damage, as well as several specialized \
                      skills (see book for skills). Thieves also may take a subclass \
                      if they qualify for it.")
    
    if class2 == "Wodewose":
        class_abil = ("Wodewose eschew civilization and embrace the Wylde. They \
                      may not use any weapons, tools, or armor that includes forged \
                      metal. They persue the agenda of nature through rituals and \
                      transformational Wild Shapes.")
        ritual2 = random.choices(ritual1, k = 3)
        shape2 = random.choice(shape1)
        class_sp = ("Wild Shape:",shape2,"Rituals:",ritual2)
        
    if class2 == "Idolator":
        class_abil = ("Expounding on the divine mysteries of the universe, \
                      Idolators have the ability to channel divine power as \
                      Orisons and can 'shun' enemies. These divine gifts come \
                      at the cost of a taboo that must be observed.")
        orison2 = random.choices(orison1, k = 3)
        taboo2 = random.choice(taboo1)
        class_sp = ("Granted Orisons:",orison2,"Taboos:",taboo2)
    print("class abilities:",class_abil,"\n",class_sp)

#Initially opens, reads, prints, and closes a txt file to instruct the user as to 
#the purpose of the script, prompts the user to start the process, calls all the
#above functions and displays them in a readable format. Finally exits the program. 
    
    
def main():
    print()
    with open("intro.txt", "r") as f:
        f_contents = f.read()
        print(f_contents)
        
    anykey = input("Press any key to begin.")
    new_pc()
    exit    
    
def new_pc():
    pc_name()
    print(race2, class2, "\n")
    str_stat(),dex_stat(),con_stat(),int_stat(),wis_stat()
    cha_stat(),armor(),hp_saves(),races(),classes()

main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:26:52 2019

@author: kynligbein
"""
#class1 = ["Magus\n","Puissant\n","Thief\n","Idolator\n","Woodwose\n"]
#
#for i, item in enumerate(class1,1):
#    print(i, ". " + item, sep="",end="\n")
import random


def str_stat():
    strength = random.randint(3,18)
    str_mod = ()
    if strength in range (3,9):
        str_mod = ("Effete!")
    elif strength in range (9,13):
        str_mod = ("Average")
    elif strength in range (13,19):
        str_mod = ("Mighty!")
    else:
        print("Something is wrong with this stat!")
    
    print("STR:",strength,str_mod)
    
    
def dex_stat():
    dexterity = random.randint(3,18)
    dex_mod = ()
    AC = ()
    if dexterity in range (3,9):
        dex_mod = ("Oafish!")
        AC = dexterity - 1
    elif dexterity in range (9,13):
        dex_mod = ("Average")
        AC = dexterity
    elif dexterity in range (13,19):
        dex_mod = ("Nimble!")
        AC = dexterity + 1
    else:
        print("Something is wrong with this stat!")
    
    print("DEX:",dexterity,dex_mod)
    print("AC: ", AC)
    
def con_stat():
    constitution = random.randint(3,18)
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
    intelligence = random.randint(3,18)
    int_mod = ()
    if intelligence in range (3,9):
        int_mod = ("Mooncalf!")
    elif intelligence in range (9,13):
        int_mod = ("Average")
    elif intelligence in range (13,19):
        int_mod = ("Canny!")
    else:
        print("Something is wrong with this stat!")
    
    print("INT:",intelligence,int_mod)   
    
    
def wis_stat():
    wisdom = random.randint(3,18)
    wis_mod = ()
    if wisdom in range (3,9):
        wis_mod = ("Foolish!")
    elif wisdom in range (9,13):
        wis_mod = ("Average")
    elif wisdom in range (13,19):
        wis_mod = ("Sophic!")
    else:
        print("Something is wrong with this stat!")
    
    print("WIS:",wisdom,wis_mod) 
    
    
def cha_stat():
    charisma = random.randint(3,18)
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
    
    
    

str_stat()
dex_stat()
con_stat()
int_stat()
wis_stat()
cha_stat()
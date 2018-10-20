#!/usr/bin/python3.5

from sys import exit

def gold_room():
    print ("gold_room")

    next = input()
    if "0" in next or  "1" in next:
        how_much = int(next)
    else:
        dead("Man,learn to type a number.")

    if how_much < 50:
        print ("less 50")
        exit(0)
    else:
        dead("great 50")

def bear_room():
    print ("bear_room")
    bear_moved = False

    while True:
        next = input()
        
        if next == "take honey":
            dead("Look at you")
        elif next == "taunt bear" and not bear_moved:
            print ("move")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("gets pissed")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print ("got no idear")

def cthulhu_room():
    print ("cthulu_room")

    next = input()
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well")
    else:
        cthulhu_room()

def dead(why):
    print ("Good job!")
    exit(0)

def start():
    print ("dark_room")
    next = input()
    if next == "left":  
        bear_room()
    elif  next == "right":
        cthulhu_room()
    else:
        dead("else")
start()
            

             
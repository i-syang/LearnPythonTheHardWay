#!/usr/bin/python3.5
name = 'Zed A. Show'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'Blue'
hair = 'Brown'

print ("Let's talk about %s." % name)
print ("He's %d inches tall." % height)
print ("He's  %d pounds heavy." % weight)
print ("Actually that's not too heavy.")
print ("He's got %s  eyes and %s hair.")
print ("His teeth are ususally %s depending on the coffe." %  teeth)

# this line is tricky,try to get it exactly right 
print ("If I add %d, %d , and %d I get %d." % (
      age,  height,   weight,   age +   height +   weight))


#!/usr/bin/python3.5

the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears', 'aoricots']
change = ['1', 'pennies', 2, 'dime', 3, 'quarters']

for number in the_count:
    print ("The is count %d " % number)

for fruit in fruits:
    print ("A fruit of type: %s" %fruit)

for i in change:
    print ("I got %r" % i)

elements =[]

for i in range(0,6):
    print ("Adding %d to the list." % i)
    elements.append(i)

for i in elements:
    print ("Element was: %d" % i)

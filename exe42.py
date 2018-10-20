#!/usr/bin/python3.5

class Parent(object):

    def impricit(self):
        print ("PARENT implicit()")

class Child(Parent):
    pass

    dad = Parent()
    son = Child()

    dad.implicit()
    son.implicit()
    
#@!/usr/bin/python3.5

print ("You enter a dark room with two doors. Do you go through door #1 or door #2")

door = input()

if door == "1":
    print ("There's a  gaint bear here eating a cake. What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input()
    if bear == "1":
        print ("if - if !")
    elif bear == "2":
        print ("if - elif bear == 2")
    else:
        print ("if - else ")

elif door == "2":
    print ("else door == 2")

    insanity = input()
    if insanity == "1" or insanity == "2":
        print("else - if")
    else:
        print("else - else")

else:
    print("else")
    
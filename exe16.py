#!/usr/bin/python3.5
from sys import argv

script ,filename = argv

print ("We're going to erase %r." %filename)
print ("If you don't want that, hit CTRL-c(^C).")
print ("If you do want that,hit RETURN.")

print ("?")

print ("Opening the file ...")
target = open(filename,'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input()
line2 = input()
line3 = input()

print ("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(%s+"\n"+%s+"\n"+%s+"\n"),%(line1,line2,lin3)
#target.write([line1,line2,line3,''].join("\n"))
#target.write( [ line1 ,line2 ,line3 ,'' ].join( '\n ' ) )

#运行报错了  


print ("And finally,we close it.")
target.close()

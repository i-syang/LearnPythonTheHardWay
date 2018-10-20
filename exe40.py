#!/usr/bin/python3.5

class Song(object):   #创建一个叫Song的类，它是对象的一种

    def __init__(self, lyrics):  #类Song有一个__init__接收self和lyrics作为参数
        self.lyrics = lyrics    
        def sing_me_a_song(self):  #类Song 有一个函数名称为sing_me_a_song，它接收self作为参数
            for line in self.lyrics:
                print (line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
#将


bulls_on_parade = Song(["Thay rally aroud the family",
                            "with pockrts full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

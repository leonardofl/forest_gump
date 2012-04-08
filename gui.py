#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2012, Leonardo Leite
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from Tkinter import *

def say_hi():
    print "hi"

class Gui(object):

    def __init__(self):
        root = Tk()
        title = Label(root, text="Forest Gump, o contador de histórias")
        title.pack()
        self.word = Label(root, text="Let's rock")
        self.word.pack()
        button = Button(root, text="Hello", command=lambda: self.print_word("hello world"))
        button.pack()
        root.mainloop()

    def print_word(self, word):
        print word

if __name__ == "__main__":

    gui = Gui()
#    Timer(self.interval, gui.print_word(), ('pirata')).start()



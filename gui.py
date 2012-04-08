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
from threading import Timer

class Interface(object):

    def __init__(self):
        self.root = Tk()
        title = Label(self.root, text="Forest Gump, o contador de histórias")
        title.pack()
        self.clock = 0
        self.clocking = False
        self.word_label = Label(self.root, text="Let's rock")
        self.word_label.pack()
        self.clock_label = Label(self.root, text=self.clock)
        self.clock_label.pack()
        
    def start(self):
        self.root.mainloop()

    def start_clock(self):
        self.clocking = True
        self.__clock()

    def __clock(self):
        self.clock += 1
        self.clock_label.configure(text=self.clock)
        if (self.clocking):
            Timer(1, self.__clock, ()).start()

    def stop_clock(self):
        self.clocking = False

    def print_word(self, word):
        self.word_label.configure(text=word)

if __name__ == "__main__":

    gui = Interface()
    gui.start()



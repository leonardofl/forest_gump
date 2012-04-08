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
from PIL import Image, ImageTk

from image_retriever import get_image

class Interface(object):

    def __init__(self):

        color = 'light salmon'
        self.clock = 0
        self.clocking = False

        self.root = Tk()
        frame = Frame(self.root, bg=color)
        frame.pack()
        title = Label(frame, text="Forest Gump, o contador de histórias", font=('times', 50, 'bold'), bg=color)
        title.pack()
        self.tkimg = ImageTk.PhotoImage(Image.open("resources/img/kiss.jpg"))
        self.image_label = Label(frame, image=self.tkimg, width=400, height=300, bg=color)
        self.image_label.pack()
        self.word_label = Label(frame, text="Let's rock!", font=('times', 100, 'bold'), bg=color)
        self.word_label.pack()
        self.clock_label = Label(frame, text=self.clock, font=('times', 70, 'bold'), bg=color)
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
        img_path = get_image(word)        
        if not img_path:
            img_path = "resources/img/nothing.png"
        self.tkimg = ImageTk.PhotoImage(Image.open(img_path))
        self.image_label.configure(image=self.tkimg)

    def stop(self):
        self.word_label.configure(text="ACABOU!")
        self.tkimg = ImageTk.PhotoImage(Image.open("resources/img/stop.jpg"))
        self.image_label.configure(image=self.tkimg)
        self.stop_clock()

if __name__ == "__main__":

    gui = Interface()
    gui.start()



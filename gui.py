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
from round import Round

COLOR = 'light salmon'

class RoundInterface(object):

    def __init__(self, names):

        self.clock = 0
        self.clocking = False
        self.names = names

        self.root = Toplevel()
        self.root.title("Forest Gump")
        frame = Frame(self.root, bg=COLOR)
        frame.pack()
        title = Label(frame, text="Forest Gump, o contador de histórias", font=('times', 50, 'bold'), bg=COLOR)
        title.pack()
        self.tkimg = ImageTk.PhotoImage(Image.open("resources/img/kiss.jpg"))
        self.image_label = Label(frame, image=self.tkimg, width=400, height=300, bg=COLOR)
        self.image_label.pack()
        self.word_label = Label(frame, text="Let's rock!", font=('times', 100, 'bold'), bg=COLOR)
        self.word_label.pack()
        self.clock_label = Label(frame, text=self.clock, font=('times', 70, 'bold'), bg=COLOR)
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
        if word in self.names:
            img_path = "resources/img/avatar.png"
        self.tkimg = ImageTk.PhotoImage(Image.open(img_path))
        self.image_label.configure(image=self.tkimg)

    def stop(self):
        self.word_label.configure(text="ACABOU!")
        self.tkimg = ImageTk.PhotoImage(Image.open("resources/img/stop.jpg"))
        self.image_label.configure(image=self.tkimg)
        self.stop_clock()

class Interface(object):

    def __init__(self, lists=[]):

        self.root = Tk()

        self.lists = lists

        self.root.title("Forest Gump")
        master_frame = Frame(self.root, bg=COLOR)
        master_frame.pack()
        title = Label(master_frame, text="Forest Gump, o contador de histórias", font=('times', 30, 'bold'), bg=COLOR)
        title.pack(side=TOP)
        left_frame = Frame(master_frame, bg=COLOR, border=10)
        left_frame.pack(side=LEFT)
        right_frame = Frame(master_frame, bg=COLOR)
        right_frame.pack(side=RIGHT)

        self.tkimg = ImageTk.PhotoImage(Image.open("resources/img/uncle_sam.jpg"))
        image_label = Label(right_frame, image=self.tkimg, width=400, height=300, bg=COLOR)
        image_label.pack(side=RIGHT)
        lists_frame = Frame(right_frame, bg=COLOR, border=5)
        lists_frame.pack(side=LEFT)

        lists_label = Label(lists_frame, text="Cartuchos", font=('times', 12), bg=COLOR, border=5)
        lists_label.pack(side=TOP)
        self.cbs = []
        self.cb_values = []
        for i, l in enumerate(self.lists):
            self.cb_values.append(IntVar())
            check = Checkbutton(lists_frame, text=l, bg=COLOR, border=5, var=self.cb_values[i])
            self.cbs.append(check)
            check.pack(side=BOTTOM)

        names_label = Label(left_frame, text="Jogadores (um por linha):", font=('times', 12), bg=COLOR, border=5)
        names_label.pack()
        self.names_text = Text(left_frame, height=10, width=40, border=5)
        self.names_text.pack()
        button_frame = Frame(left_frame, border=5, bg=COLOR)
        button_frame.pack()
        name_button = Button(button_frame, text="Inicia rodada", command=self.start_round)
        name_button.pack()

    def start(self):
        self.root.mainloop()

    def start_round(self):
        names = self.__get_names()
        lists = self.__get_selected_lists()
        interface = RoundInterface(names)
        round = Round(5, 2, names, lists, interface)
        round.start()

    def __get_names(self):        
        names_str = self.names_text.get(1.0, END)
        names = names_str.splitlines()
        return names

    def __get_selected_lists(self):
        selected = []
        for i, l in enumerate(self.lists):
            if self.cb_values[i].get():
                selected.append(l) 
        return selected


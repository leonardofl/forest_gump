#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
frame = Frame(root)
frame.pack()
img = Image.open("resources/img/python.png")
tkimg = ImageTk.PhotoImage(img)
image_label = Label(frame, image=tkimg)
image_label.pack()
root.mainloop()


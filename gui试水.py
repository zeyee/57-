#!/usr/bin/env python
#coding=utf-8

from Tkinter import*
from os.path import exists
from PIL import Image, ImageTk
print exists(r'/Users/wsc/Downloads/b348d470-dc1a-4370-8911-3edcb25d3d23.png')
top = Tk()
top.geometry('200x200')
wifi_img = Image.open(r"/Users/wsc/Downloads/b348d470-dc1a-4370-8911-3edcb25d3d23.png")
print wifi_img
photo = ImageTk.PhotoImage(wifi_img)
print photo
label = Label(top, image=wifi_img)
label.pack()
top.mainloop()

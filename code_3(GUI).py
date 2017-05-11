#!/usr/bin/env python
#coding=utf-8

from Tkinter import *

def comulate(ev=None):
    a = label3.get()
    label2.config(text='%s has %d characters.' % (a, len(a)))
    label2.grid(row=2, sticky='w',columnspan=3000)

top = Tk()
top.title('hello')
label1 = Label(top, text='What is the input string? ', bg='blue')
label2 = Label(top, text='')
label3 = Entry(top, relief='raised', foreground='blue', font= ('Helvetica', '14', 'bold'))
button = Button(top, text='确定', command=comulate)
label1.grid(row=0, sticky='w')
label3.grid(row=0, column=10)
button.grid(row=1, sticky='w', columnspan=3000)

top.mainloop()


#!/usr/bin/env python
#coding=utf-8

import re
from Tkinter import *
def count1(ev=None):
    label1.config(text='What is the length of the room in feet? ')
    label1.grid(row=3,sticky='w')
    enter1.grid(row=3,column=20)
    label2.config(text='Whay is the width of the room in feet? ')
    label2.grid(row=4,sticky='w')
    enter2.grid(row=4,column=20)
    button3.grid(row=5)
    label3.config(text='')

def count(ev=None):
    a = enter1.get()
    b = enter2.get()
    if re.match('\d+\.\d+$', a) or re.match('\d+$', a):
        a = float(a)
        if re.match('\d+\.\d+$', b) or re.match('\d+$', b):
            b = float(b)
            sum = a * b
            sum = sum * 0.09290304
            if sum % 0.001 >= 0.0005:
                sum = int(sum * 1000 + 1) / 1000.
            else:
                sum = int(sum * 1000) / 1000.

            label3.config(text='The area is\n%.3f square feet\n%.3f square meters' % ((a * b), sum))
            label3.grid(row=6, sticky='w')
        else:
            label3.config(text='输入错误。')
            label3.grid(row=6, sticky='w')
    else:
        label3.config(text='输入错误。')
        label3.grid(row=6, sticky='w')



def count2(ev=None):
    label1.config(text='What is the length of the room in meter? ')
    label1.grid(row=3, sticky='w')
    enter1.grid(row=3, column=20)
    label2.config(text='Whay is the width of the room in meter? ')
    label2.grid(row=4, sticky='w')
    enter2.grid(row=4, column=20)
    button4.grid(row=5)
    label3.config(text='')

def count3(ev=None):
    a = enter1.get()
    b = enter2.get()
    if re.match('\d+\.\d+', a) or re.match('\d+', a):
        a = float(a)
        if re.match('\d+\.\d+$', b) or re.match('\d+$', b):
            b = float(b)
            sum = a * b
            sum = sum/0.09290304
            label3.config(text='The area is\n%.3f square meters\n%.3f square feet' % ((a * b), sum))
            label3.grid(row=6, sticky='w')
        else:
            label3.config(text='输入错误。')
            label3.grid(row=6, sticky='w')
    else:
        label3.config(text='输入错误。')
        label3.grid(row=6, sticky='w')

top = Tk()
top.geometry('600x200')
top.title('矩形房间的面积。')
label0 = Label(top, text='feet or meter? ')
label0.grid(row=0, sticky='w')
#label0.grid_forget()
button1 = Button(top, text='feet', command=count1)
button1.grid(row=1,sticky='w')
button2 = Button(top, text='meter', command=count2)
button2.grid(row=1,column=1)
button3 = Button(top,text='计算1',command=count)
button4 = Button(top,text='计算2',command=count3)
label1 = Label(top, text='')
enter1 = Entry(top)
label2 = Label(top, text='')
enter2 = Entry(top)
label3 = Label(top, text='')
top.mainloop()
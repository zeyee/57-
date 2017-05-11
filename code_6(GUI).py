#!/usr/bin/env python
#coding=utf-8
from Tkinter import *
import re
def jian(ev=None):
    if re.match(r'[+-]?\d+$', enter1.get()) and re.match(r'[+-]?\d+$', enter2.get()):
        a = int(enter1.get())
        b = int(enter2.get())
        print type(enter1.get())
        label7.config(text="")
        label3.config(text='%d - %d = %d' % (a, b, a-b))
        label3.grid(row=3,column=0,sticky='w')
        label4.config(text='%d + %d = %d' % (a, b, a+b))
        label4.grid(row=4,column=0,sticky='w')
        label5.config(text='%d * %d = %d' % (a, b, a * b))
        label5.grid(row=5,column=0,sticky='w')
        label6.config(text='%d / %d = %d' % (a, b, a / b))
        label6.grid(row=6,column=0,sticky='w')
    else:
        label3.config(text='')
        label4.config(text='')
        label5.config(text='')
        label6.config(text='')
        label7.config(text="你输入的不是数字.")
        label7.grid(row=3)

top = Tk()
label1 = Label(top, text="What's the first number? ")
label2 = Label(top, text="what's the second number? ")
label3 = Label(top, text="")
label4 = Label(top, text="")
label5 = Label(top, text="")
label6 = Label(top, text="")
label7 = Label(top, text="")
enter1 = Entry(top)
enter2 = Entry(top)
button1 = Button(top, text='四则运算', command=jian)
label1.grid(sticky='w')
enter1.grid(row=0,column=20)
label2.grid(sticky='w')
enter2.grid(row=1,column=20)
button1.grid(row=2,column=20)
top.mainloop()
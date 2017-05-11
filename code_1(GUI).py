#!/usr/bin/env python
# coding=utf-8

from Tkinter import *


def resize(ev=None):
    label.config(text='小费比例:%d%c' % (scale.get(), '%'))


def caculate(ev=None):
    a = scale.get()
    b = float(e_user.get())
    print type(b)
    print b
    if (isinstance(b, float) or isinstance(b, int)) and b >= 0:
        c = b * a / 100.
        print 'xx'
        # print type(c)
        if c % 0.01 >= 0.001:
            c = c - c % 0.001
        label1.config(text='小费金额:$%.2f' % c)
        label2.config(text='总金额:$%.2f' % (b + c))
    else:
        l_msg['text'] = '我喜欢你。'
        label1.config(text='小费金额:输入金额错误无法计算')
        label2.config(text='总金额:输入金额错误无法计算')


top = Tk()
top.geometry('300x200')
l_user = Label(top, text='用户金额：')
l_user.grid(column=0, row=0, rowspan=2, sticky='w')
e_user = Entry(top)
e_user.grid(column=7, row=0, rowspan=2, sticky='w')
label = Label(top, text='小费比例:')
label.grid(column=0, row=3, rowspan=2, sticky='w')
label1 = Label(top, text='小费金额：')
label2 = Label(top, text='总金额：')
label1.grid(column=0, columnspan=3000, sticky='w')
label2.grid(column=0, columnspan=3000, sticky='w')
scale = Scale(top, from_=0, to=100, orient=HORIZONTAL, command=resize, fg='blue')
scale.set(0)
scale.grid(column=0, columnspan=3000, sticky='ew')
button = Button(top, text='计算', command=caculate, fg='red')
button.grid(column=0, sticky='w')
l_msg = Label(top, text='')
l_msg.grid(sticky='w')
# scale.rowconfigure(30,weight=30)

top.mainloop()
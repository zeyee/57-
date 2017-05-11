#!/usr/bin/env python
#coding=utf-8

import re
a = raw_input("How many people? ")
sum = 0
if re.match(r"\d+$", a):
    a = int(a)
    b = raw_input("How do you divided? ")
    if re.match(r"\d+$", b):
        #print "a"
        b = int(b)
        c = []
        for i in range(a):
            d = raw_input("How many pieces do you want? ")
            if re.match(r'\d+$', d):
                d = int(d)
                c.append(d)
            else:
                print"输入错误，请重新输入。"
                i -= 1
        for i in range(a):
            #print type(c[i])
            sum += c[i]
        if sum%b == 0:
            print "需购买数量：%d" % (sum/b)
        else:
           print "需购买数量：%d" % (sum/b+1)
    else:
        print "输入错误."
else:
    print "输入错误。"
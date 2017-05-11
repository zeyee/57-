#!/usr/bin/env python
#coding=utf-8
def count():
    global sum
    print "%d" %sum
    for i in range(len(a1)):
        sum = sum + a1[i]*b1[i]
import re
a1 = []
b1 = []
a = raw_input("Enter the price of item 1: ")
if re.match(r'\d+$', a):
    a = float(a)
    a1.append(a)
    b = raw_input("Enter the quantity of item 1: ")
    if re.match(r'\d+$', b):
        b = float(b)
        b1.append(b)
        c = raw_input("Enter the price of item 2: ")
        if re.match(r'\d+$', c):
            c = float(c)
            a1.append(c)
            d = raw_input("Enter the quantity of item 2: ")
            if re.match(r"\d+$", d):
                d = float(d)
                b1.append(d)
                e = raw_input("Enter the price of item 3: ")
                if re.match(r'\d+$', e):
                    e = float(e)
                    a1.append(e)
                    f = raw_input("Enter the quantity of item 3: ")
                    if re.match(r'\d+$', f):
                        f = float(f)
                        b1.append(f)

for i,j in zip(a1,b1):
    print "%.2f" % i
    print "%.2f" % j
sum = 0
count()
print "Subotal: $%.2f" % sum
print "Tax: $%.2f" % (sum*0.055)
print "Total: $%.2f" % (sum + sum*0.055)
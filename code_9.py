#!/usr/bin/env python
#coding=utf-8

import re
a = raw_input("How many people? ")
if re.match(r'\d+$', a):
    a = int(a)
    b = raw_input("How many pizzas do you have? ")
    if re.match(r'\d+$', b):
        b = int(b)
        e = raw_input("How do you divide? ")
        if re.match(r'\d+$', e):
            e = int(e)
            c = e*b/a
            if c%1>0:
                c = int(c+1)
            else:
                c = int(c)
            d = b*e - a*c
            if a > 1 and b>1:
                print "%d people with %d pizzas" % (a, b)
                if c>1:
                    print "Each person gets %d pieces of pizza." % c
                    if d>1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
                else:
                    print "Each person gets %d piece of pizza" % c
                    if d>1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
            elif a>1 and b<= 1:
                print "%d people with %d pizza" % (a, b)
                if c>1:
                    print "Each person gets %d pieces of pizza." % c
                    if d>1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
                else:
                    print "Each person gets %d piece of pizza" % c
                    if d>1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
            elif a==1 and b>1:
                print "%d person with %d pizzas" % (a, b)
                if c > 1:
                    print "Each person gets %d pieces of pizza." % c
                    if d > 1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
                else:
                    print "Each person gets %d piece of pizza" % c
                    if d > 1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
            else:
                print "%d person with %d pizza" % (a, b)
                if c > 1:
                    print "Each person gets %d pieces of pizza." % c
                    if d > 1:
                         print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d
                else:
                    print "Each person gets %d piece of pizza" % c
                    if d > 1:
                        print "There are %d leftover pieces." % d
                    else:
                        print "There is %d leftover piece." % d

        else:
            print("输入错误。")
    else:
        print("输入错误。")
else:
    print("输入错误。")

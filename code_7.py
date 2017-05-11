#!/usr/bin/env python
#coding=utf-8

import datetime

a = input("What is your current age? ")
b = input("At what age would you like to retire? ")
c = datetime.datetime.now().year
if (b-a)>=0:
    print "You have %d years left until you can retire." % (b-a)
    print "It's %d, so you can retire in %d" % (c, c+b-a)
else:
    print "你已经可以退休了。"
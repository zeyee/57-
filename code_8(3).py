#!/usr/bin/env python
# coding=utf-8
import re
def suan(sum):
    print c
    if c is 'f':
        sum = sum * 0.09290304
        if sum % 0.001 >= 0.0005:
            sum = int(sum * 1000 + 1) / 1000.
        else:
            sum = int(sum*1000)/1000.
    else:
        sum = int(sum/0.09290304)
    print sum
    return sum
c = raw_input("feet or meter(f or m)? ")
if c == 'f':
    a = raw_input("What is the length of the room in feet? ")
    if re.match(r"\d+",a) is not None:
        a = int(a)
        b = raw_input("What is the width of the room in feet? ")
        if re.match(r"\d+",b) is not None:
            b = int(b)
            print "You entered dimensions of %d feet by %d feet." % (a, b)
            print "The area is "
            print "%d sqare feet" % (a * b)
            print "%.3f square meters" % suan(a * b)
        else:
            print "输入错误。"
    else:
        print "输入错误。"
elif c == 'm':
    a = raw_input("What is the length of the room in meter? ")
    if re.match(r"\d+.", a):
        a = float(a)
        b = raw_input("What is the width of the room in meter? ")
        if re.match(r"\d+.", b) :
            b = float(b)
            print "You entered dimensions of %.3f feet by %d meter." % (a, b)
            print "The area is "
            print "%.3f sqare feet" % (a * b)
            print "%.3f square feet" % suan(a * b)
        else:
            print "输入错误。"
    else:
        print "输入错误。"
else:
    print "输入错误。"
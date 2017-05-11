#!/usr/bin/env python
#coding=utf-8
import re
def count():
    print "%d + %d = %d" % (int(a), int(b), int(a+b))
def jian():
    print "%d - %d = %d" % (int(a), int(b), int(a - b))

def cheng():
    print "%d * %d = %d" % (int(a), int(b), int(a * b))

def chu():
    print "%d / %d = %d" % (int(a), int(b), int(a / b))
a = raw_input("What is the first number? ")
b = raw_input("what is the second number? ")
if re.match(r"\d+$", a) and re.match(r"\d+$",b):
    count()
    jian()
    cheng()
    chu()
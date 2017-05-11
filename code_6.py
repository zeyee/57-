#!/usr/bin/env python
#coding=utf-8
a = raw_input("What is the first number? ")
b = raw_input("what is the second number? ")
a = float(a)
b = float(b)
print "%.0f + %.0f = %.0f\n%.0f - %.0f = %.0f\n%.0f * %.0f = %.0f\n%.0f / %.0f = %.0f " \
    % (a, b, a+b, a, b, a-b,a,b,a*b,a,b,a/b)

#!/usr/bin/env python
#coding=utf-8

a = raw_input("What is the input string? ")
if len(a) is 0:
    print '请你输入内容.'
    a = raw_input("what is the input string? ")

print "%s has %d characters." % (a, len(a))
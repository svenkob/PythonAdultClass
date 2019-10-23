#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73
print("test")

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))


def x():
    print("x")
    def y():
        print("y")
    y()

x()

def x():
    x=100
    x()
#!/usr/bin/python
# -*- coding: UTF-8 -*-



def do_main():
    max = 0

    for i in range(1,101):
        tmp = (5050-i) * i
        max += tmp
    print max

#!/usr/bin/python
# -*- coding: UTF-8 -*-

def ispalindrome(n):
    st = str(n)
    vers =st[::-1]
    if st == vers:
        return True
    return False


def do_main():
    max = 0
    a = 0
    b = 0
    for i in range(100,999):
        for j in range(100,999):
            multi = i*j
            if ispalindrome(multi) == True and multi > max:
                max = multi
                a = i
                b = j
    print max," == ",a," * ",b

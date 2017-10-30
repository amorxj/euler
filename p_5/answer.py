#!/usr/bin/python
# -*- coding: UTF-8 -*-

def addPrimeFactor(dict,prim,number):
    st = str(prim)
    n = dict.get(st,0)
    if n < number:
        dict[st] = number
    return

def divN(n,dict):
    factor=2
    lastFactor=1
    factor_n = 0
    if n%2 == 0:
        n = n/2
        lastFactor =2
        factor_n += 1
        while n%2==0:
            n = n/2
            factor_n+=1
        addPrimeFactor(dict,lastFactor,factor_n)
    factor =3
    factor_n = 0
    while n>1 and factor*factor<=n :
        if n % factor ==0:
            lastFactor=factor
            n=n/factor
            factor_n+=1
            while n %factor==0:
                n=n/factor
                factor_n+=1
            addPrimeFactor(dict,lastFactor,factor_n)
        factor=factor+2
        factor_n = 0

    if n == 1 :
        pass
    else:
        addPrimeFactor(dict,n ,1 )

def do_main():
    dict= {}
    for i in range(2,21):
        divN(i,dict)
        print i,"----\n",dict

    mutil = 1
    for s,t in dict.iteritems():
        number = int(s)
        for j in range(0,t):
            mutil *=number

    print mutil

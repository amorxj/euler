#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = 600851475143 ## eta 47秒完成
lastNotPrime = 2
primeList =[ 2 ]

class primeFinde(object):
    """拥有查找质数."""
    def __init__(self):
        self.primeDict= {'2':2}
    def isPrime(self,n):
        name = str(n)
        if self.primeDict.has_key(name):
            return True
        else:
            for st,value in self.primeDict.iteritems():
                if n%value == 0:
                    return False
            self.primeDict[name]=n
            return True

p3 = primeFinde()
def isPrime3(n):
    return p3.isPrime(n)

def isPrime2(n):
    global primeList
    for value in primeList:
        if n%value == 0:
            return False
    primeList.append(n)
    return True

def isPrime(n):
    global primeList
    global lastNotPrime
    if n<2:
        return False
    try:
        if primeList.index(n) > 0:
            return True
    except Exception as e:
        pass

    if primeList[-1] >= n:
        return False

    # if n <=lastNotPrime :
    #     return False

    largest = n/2
    i = 2
    while i<largest:
        if n%i == 0:
            return False
        i+=1
    primeList.append(n)
    return True

def do_main():
    global num
    maxPrime=None
    i = 2;
    factor = []
    while i<=num/2:
        if num%i == 0 :
            if isPrime3(i) :
                maxPrime = i
                if i*i > num:
                    break
            else:
                factor.insert(0,i)
        i+=1
    if maxPrime == None:
        print "cant' find max prime for ",num," and all factor is \n"
        print factor
    else:
        print maxPrime
    return True

if __name__ == '__main__':
    print do_main()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = 9999991111101  ## eta 47秒完成
# num = 600851475143/10
#num = 10976461
# num = 54499
lastNotPrime = 2
primeList =[ 2 ]

def do_main():
    global num
    n=num
    factor=2
    lastFactor=1
    if n%2 == 0:
        n = n/2
        lastFactor =2
        while n%2==0:
            n = n/2
    factor =3
    while n>1 and factor*factor<n :
        if n % factor ==0:
            lastFactor=factor
            n=n/factor
            while n %factor==0:
                n=n/factor
            if lastFactor * lastFactor > n:
                pass
        factor=factor+2
        
    if n == 1 :
        print lastFactor
    else:
        print n


def do_main2():
    global num
    n=num
    factor=2
    lastFactor=1
    while n>1:
        if n % factor ==0:
            lastFactor=factor
            n=n/factor
            while n %factor==0:
                n=n/factor
        factor=factor+1
    print lastFactor

class primeFinde(object):
    """学习并查找质数"""
    def __init__(self):
        self.primeDict= {'2':2}
        self.primeList= [2]
        # self.maxLearn = 2

    # def minPrimeFactor(self,n):
    #     for value in self.primeList:
    #         if n%value == 0 :
    #             return value
    #         if value*value>n:
    #             break;
    #     return n

    def isPrime(self,n):
        name = str(n)
        if self.primeDict.has_key(name):
            return True
        else:
            for value in self.primeList:
                if n%value == 0 :
                    return False
                if value*value>n:
                    break;
            self.primeList.append(n)
            self.primeDict[name]=n
        return True
    def getPrimeList(self):
        return self.primeList


p3 = primeFinde()
def isPrime3(n):
    return p3.isPrime(n)

def printPrim():
    print p3.getPrimeList()

def printLastPrim():
    print "No is ",len(p3.getPrimeList())


def do_main3():
    global num
    maxPrime=None
    i = 2;
    factor = []
    goal = num
    while i<=goal:
        if i*2>goal:
            maxPrime = goal
            break
        elif isPrime3(i) :
            if goal%i == 0 :
                if i > maxPrime:
                    maxPrime = i
                if i*i > goal:
                    break
                else:
                    while goal%i == 0:
                        goal = goal/i
                        print "goal become smaller ",goal,"and i= ",i
                        printPrim()

        i+=1

    printLastPrim()

    if maxPrime == None:
        print "cant' find max prime for ",num," and all factor is \n"
        print factor
    else:
        print maxPrime
    return True

if __name__ == '__main__':
    print do_main()

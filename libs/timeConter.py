#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import threading

class TimeConter(object):
    """计算时间的"""
    def __init__(self, func,timeout):
        self.func = func
        self.timeout = timeout

    def runFunc(self):
        t0  = time.clock()

        th = threading.Thread(target = self.func)
        th.setDaemon(True)
        th.start()
        th.join(timeout = self.timeout)

        t1 = time.clock() -t0
        if th.isAlive():
            print "#####[ERROR]: run %d seconds , time out! " %t1
        else:
            print "#####[OK   ]: consum time= %d "%t1

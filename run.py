#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt
from libs import timeConter
import importlib

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"n:t:")
    except getopt.GetoptError:
        print "can't find answers of arg"

    timeout =  20## 秒
    model = None
    for opt,value in opts:
        if opt == '-n':
            model = 'p_'+ value +'.answer'
        elif opt == '-t':
            timeout = int(value)
    if model!=None:
        answer = importlib.import_module(model)
        t = timeConter.TimeConter(answer.do_main, timeout)
        t.runFunc()
    else:
        print "can't find problem number"

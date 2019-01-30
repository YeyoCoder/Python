# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:46:30 2019

@author: olver
"""
P=set([2])
n=3
while len(P) < 10:
    doAdd = True
    for d in P:
        if n % d == 0 and doAdd:
            doAdd = False
    if doAdd:
        P.add(n)           
    n += 1
print(P)
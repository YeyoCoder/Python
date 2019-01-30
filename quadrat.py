# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:16:55 2019

@author: olver
"""
import math
print("Resolver ax^2 + bx + c = 0")
while True:
    try:
        a=float(input("a = "))
        break
    except ValueError:
        print("Introduce un número de punto flotante")
while True:
    try:
        b=float(input("b = "))
        break
    except ValueError:
       print("Introduce un número de punto flotante")
while True:
    try:
        c=float(input("c = "))
        break
    except ValueError:
        print("Introduce un número de punto flotante")
        
d = b**2-4 - 4*a*c
if d >= 0:
    x1=(-b+math.sqrt(d)) / (2* a)
    x2=(-b-math.sqrt(d)) / (2* a)
    print("x1 = {}, x2 = {}".format(x1,x2))
else:
    re = -b / (2 * a)
    im = math.sqrt(-d) / (2 * a)    
    print("x1 = {} + {}i, x2 = {} - {}i".format(re,im,re,im))
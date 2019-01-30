# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:16:55 2019

@author: olver
"""
import math

def input_float(string):
    while True:
        try:
            return float(input(string))
            break
        except ValueError:
            print("Introduce un número de punto flotante")
            
print("Resolver ax^2 + bx + c = 0")
a = input_float("a = ")
b = input_float("b = ")
c = input_float("c = ")

d = b**2 - 4*a*c
if d >= 0:
    try:
        x1=(-b+math.sqrt(d)) / (2* a)
        x2=(-b-math.sqrt(d)) / (2* a)
        print("x1= {}, x2 = {}".format(x1,x2))
    except ZeroDivisionError:
        try:
            print("x={}".format(-c/ b))
        except ZeroDivisionError:
            if c == 0:
                print("Hay infinitas soluciones")
            else:
                print("No hay solución")                
else:
    re = -b / (2 * a)
    im = math.sqrt(-d) / (2 * a)    
    print("x1 = {} + {}i, x2 = {} - {}i".format(re,im,re,im))
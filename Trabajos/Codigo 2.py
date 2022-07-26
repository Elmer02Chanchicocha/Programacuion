# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:55:16 2022

@author: S7
"""

def mayor (a,b):
    mayor=b
    
    if (a>b):
        mayor = a
    return mayor 
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))

if a>b:
    if a>c:
        print("El mayor de los tres números es: ", a)
if b>c:
    if b>a:
        print("El mayor de los tres números es: ", b)
if c>b:
    if c>a:
        print("El mayor de los tres números es: ", c)
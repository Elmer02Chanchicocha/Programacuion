# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 19:04:34 2022

@author: S7
"""


num = input("Ingrese el numero que desea evaluar: ")
def palindromo(num):
    inicio = 0
    fin = len(num) - 1
    while num[inicio] == num[fin]:
        if inicio >= fin:
            print('Es palindromo')
            return True
        else: 
            inicio += 1
            fin -= 1
    print('No es palindromo')
    return False
print(palindromo(num))
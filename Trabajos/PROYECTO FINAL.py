# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:15:01 2022

@author: HP
"""

opcion_medidas=int(input("******* MENU PRINCIPAL ******\n1 MEDIDAS DE LONGITUD\n2. MEDIDAS DE VOLUMEN"
                         "\n3. MEDIDAS DE PESO\n4. MEDIDAS DE TEMPERATURA.\nEscoja la opcion que desea :"))

if opcion_medidas ==1:
    
    print("\n*** MEDIDAS DE LONGITUD ***\n")
    opcion_submenu=int(input("1. Pulgadas a milimetros \n2. Yardas a metros \nEscoja la opcion que desea:"))
    

    if opcion_submenu ==1:
        print("--------------------------------------------------")       
        pulgadas=int(input("Ingrese la cantidad de pulgadas a convertir: "))
        milimetros= pulgadas*25.40
        print(pulgadas," Pulgadas equivalen a",milimetros,"milimetros")
        
    elif opcion_submenu ==2:
        print("------------------------------")
        yardas=int(input("Ingrese la cantidad de yardas a convertir: "))
        metros= yardas*0.9144
        print(yardas, "yardas  equivalen a",metros,"metros")
    
    else :
        print("La opcion escogida no es validad. ")
           
elif opcion_medidas ==2:
    

   print("\n\n***** MEDIDA DE VOLUMEN *******\n\n")
   
   opcion_submenu=int(input("1. pies^3 a metros^3 \n2. yarda^3 a metros^3 \nEscoja la opcion que desea:  "))
   
   if opcion_submenu ==1:
       print("--------------------------------------------------")       
       pies_3=int(input("Ingrese la cantidad de pie^3 a convertir: "))
       metros_3= pies_3*0.02832
       print(pies_3," pie^3 equivalen a",metros_3,"metros^3")
       
       
   elif opcion_submenu ==2:
       print("------------------------------")
       yardas_3=int(input("Ingrese la cantidad de yardas^3 a convertir: "))
       metros_3= yardas_3*0.7646
       print(yardas_3, "yardas^3  equivalen a",metros_3,"metros^3")
       
   else:
       print(" La opcion escogida no ers valida ") 
       
       
elif opcion_medidas ==3: 
    
    print("\n***** MEDIDAS DE PESO  *******\n")
    opcion_submenu=int(input("1. onza a gramos \n2. libras a kilogramos \nEscoja la opcion que desea:  "))
    
    if opcion_submenu ==1:
        print("--------------------------------------------------")       
        onzas=int(input("Ingrese la cantidad de onzas a convertir: "))
        gramos= onzas* 28.35
        print(onzas," onzas equivalen a",gramos,"gramos")
        
        
    elif opcion_submenu ==2:
        print("------------------------------")
        libras=int(input("Ingrese la cantidad de libras a convertir: "))
        kilogramos= libras*0.45359
        print(libras, "libras  equivalen a",kilogramos,"kilogramos")
        
    else:
        print(" La opcion escogida no ers valida ") 
        
elif opcion_medidas ==4:
    print("\n ******MEDIDAS DE TEMPERATURA******\n")
    
    def cels_a_fahr(c):
        return (c*1.8)+32
    def farhr_a_cels(f):
        return (f-32)/1.8
    def menu( ):
        print("----------------------------")
        print("1.Fahrenit a celsius ")
        print("2. Celsius a Fahrenheit")
        print("3. salir")
        opcion= input("--->")
        return opcion
def pedir_grados(escala):
    if escala == "1":
        grados = float(input("Ingrse el valor de °F: "))
    elif escala == "2":
        grados = float(input("Ingrese el valor de °C:"))
    return grados 
def mostrar_resultados(escala,grados):
    if escala =="1":
        print("Son",grados, "Celsius")
    elif escala == "2":
        print("Son",grados, "Fahrenheit")
        
while True:
    op = menu()
    if op == "3":
        break
    elif op=="1" or op == "2":
        gr = pedir_grados(op)
        if op == "1":
            conversion= farhr_a_cels(gr)
        if op == "2":
            conversion= cels_a_fahr(gr)
            mostrar_resultados(op, conversion)
    else:
        print("Introduce una opcion correcta")
        break
        
            

else:
     print(" La opcion escogida no ers valida ") 


    
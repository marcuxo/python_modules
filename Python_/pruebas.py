import time
import subprocess
import os
import sys


def pruebaTiempo():
    #texto = str(input('ingresa texto: '))
    numero = int(input('ingresa numero: '))
    print("Son "+str(numero)+" vueltas")

    cont = 0
    while cont<numero:
        print('numero vuelta: '+str(cont+1))
        print("siguiente vuelta en 5 segundos")
        time.sleep(5)
        cont = cont +1

    print('fin')
    #exit()
    menu_()


def pruebaIf():
    theTuple = ("manzana", "platano", "cherry")
    busq = str(input("Ingresa la fruta a buscar en el canasto de frutas: "))
    if busq in theTuple:
        print("**************************************")
        print("Si, aqui esta "+busq+" GANASTE!!")
        print("**************************************")
    else:
        print("No, no se encuentra")
    menu_()

def iva_():
    iva = 12
    costo = int(input('¿Cual es el monto a calcular?: '))
    calculo = costo * iva / 100
    print ("El calculo de IVA es: " + str(calculo) + "\n")
    menu_()


def menu_():       
    print("=====================")
    print("( 1 )-Prueba de timming.")
    print("( 2 )-Prueba de busqueda en tupla mediante if")
    print("( 3 )-Calcular el iva")
    print("( 4 )-Correr Servidor Ubuntu 16.x")
    print("( 10 )-Salir")
    otn = int(input("Ingresa el numero de la Opcion: "))
    
    if(otn == 1):
        pruebaTiempo()
    if(otn == 2):
        pruebaIf()
    if(otn == 3):
        iva_()
    if(otn == 4):
        ejecutarP_()
    if(otn == 10):
        exit()
    else:
        print("Opcion no valida")
    menu_()

def ejecutarP_():
    #os.startfile('c:/Users/Paico/Desktop/Python_/inicio.lnk')
    os.startfile('c:/Users/Paico/Desktop/serverOS.lnk')
    sys.exit()

print("///////////////////////////////////marcuXo\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
menu_()

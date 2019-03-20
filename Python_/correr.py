import os
import sys
import subprocess

def Civa_():
    iva = 12
    costo = int(input('Cual e sel Monto a calcular?: '))
    calculo = costo * iva / 100
    ivamas = costo + calculo
    print('El calculo de IVA es: ' + str(calculo))
    print('El calculo IVA incluido: ' + str(ivamas))
    menu_()

def ejecutarFS():
    os.system('dataFS.bat')
    sys.exit()
    
def ejecutarOS_():
    os.startfile('data2.bat')
    sys.exit()

def ejecutarXamp():
    os.startfile('xampOpen.bat')
    sys.exit()

def menu_():
    print('_____________________')
    print('(1) Calcular IVA.')
    print('(2) Correr PhotoShopCs3 Portable.')
    print('(3) Correr Servidor Web Ubuntu.')
    print('(4) Correr Xampp')
    print('(0) salir.')

    optn = int(input('Que deseas Hacer?: '))
    if(optn == 0):
        sys.exit()
    if(optn == 1):
        Civa_()
    if(optn == 2):
        ejecutarFS()
    if(optn == 3):
        ejecutarOS_()
    if(optn == 4):
        ejecutarXamp()
    else:
        print('Opcion no VALIDA')
    menu_()

menu_()

import datetime
import os

x = datetime.datetime.now()
def datos():
#------------------validar mes------------------------>
    segi4 = True
    while segi4:
        mes1 = str(input("Ingrese el mes: ")).strip()
        mes = mes1.lower()
        if mes.isalpha() == False:
            print ("Ingrese el mes (EJ: marzo)")
            degi3 = True
        elif mes == "enero" or mes == "febrero" or mes == "marzo" or mes == "abril":
            mes = mes
            segi4 = False
        elif mes == "mayo" or mes == "junio" or mes == "julio" or mes == "agosto":
            mes = mes
            segi4 = False
        elif mes == "septiembre" or mes == "octubre" or mes == "noviembre" or mes == "diciembre":
            mes = mes
            segi4 = False
        else:
            segi4 = True
    #print (mes)
    os.system('cls') # Window
    #------------fin validar mes------------------------->
            
#----VERIFICAR AÑO----------------------------------->
    segi5 = True
    while segi5:
        ano = input("Ingrese el año: ").strip()
        if ano.isdigit() == False:
            print ("el año no puede ser mayor al año actual. ",x.year)
            #segi5 = True
        elif int(ano) > int(x.year):
            print ("el año no puede ser mayor al año actual. ",x.year)
            segi5 = True
        else:
            ano = ano
            segi5 = False
    #----VERIFICAR AÑO----------------------------------->
    
    #rut = input("Rut del Trabajador: ")
    #nmb = str(input("Nombre Del Trabajador: "))
    #-----------------------categoria-->
    print ("\ncategorias de trabajadores\t")
    print ("\ta.Novato - b.Experto - c.Supervisor - d.Administrativo\t")
    segi2 = True
    while segi2:
        cat = str(input("Categoria: ")).strip()
        if cat == "b" or cat == "B":
            catp = 5000
            segi2 = False
        elif cat == "a" or cat == "A" or cat == "c" or cat == "C" or cat == "d" or cat == "D":
            cat = ""
            segi2 = False
        else:
            print ("Las opciones validas son solo a,b,c,d")
            segi2 = True
    #--------------------------------------fin categoria-->
    segi3 = True
    while segi3:
        dif = input("Dias ausentes: ").strip()
        if dif.isdigit() == False:
           print ("Ingrese un numero entre 1 y 30")
           sigi3 = True
        elif int(dif) >= 1 and int(dif) <= 30:
            segi3 = False
        else:
            print ("Ingrese un numero entre 1 y 30")
            segi3 = True
            
    afp = str(input("AFP: "))
    sal = str(input("Sistema de salud: "))
    sld = int(input("Monto Sueldo Bruto: $"))

    #----------------calculo sueldo liquido--------------------->
    #descuento afp
    afps = sld * 0.1
    #descuento distintos sys salud
    sala = sld * 0.057
    salb = sld * 0.061
    salc = sld * 0.065

    
    #si no falto niun dia +50mil
    difp = 50000
    #si categoria es experto el bono es doble
    catp = 100000
    
    

    
    

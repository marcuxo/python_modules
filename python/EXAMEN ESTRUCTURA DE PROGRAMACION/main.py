import acces
import menus

#-----------datos
import datetime

x = datetime.datetime.now()
#----------datos


mn = menus
ac = acces
print ("user-admin123")
 

 #<------------b ---control de acceso----- ---------------->
"""
print ("\t\nAcceso al software")
segi0 = True
while segi0:
    usr = input("Ingrese su usuario: ").strip()
    pasw = input("Ingrese su pasword: ")
    segi0 = ac.controlacces(usr,pasw) 
"""    
mn.menu()
"""
#<---------------menu--------------------->
datitos = datas.ingDATOS()
print ("lista",datitos)
#mn.menu()

#<---------------opciones de menu--------------------->

#dato = mn.opciones()


#print (dato)
#<---------------ingreso de datos---------------------> 
segi4 = True
while segi4:
    a = str(input("ingrese mes: "))
    mes = a.lower()
    meses = ("enero","febrero","marzo","abril","mayo","junio","julio",
         "agosto","septiembre","octubre","noviembre","diciembre")
    if mes in meses:
        segi4 = False
    else:
        print ("ingrese un mes valido")
    
    #------------fin validar mes------------------------->
            
#----VERIFICAR AÑO----------------------------------->
segi5 = True
minm = 1950
while segi5:
    ano = input("Ingrese el año: ").strip()
    if ano.isdigit() == False:
        print ("el año no puede ser mayor al año actual. ",x.year)
        segi5 = True
        
    elif int(ano) < int(minm) or int(ano) > int(x.year):
        print ("el año no puede ser mayor al año actual. ",x.year)
        segi5 = True
    else:
        segi5 = False
    #----VERIFICAR AÑO----------------------------------->

        
    
rut = input("Rut del Trabajador: ")
nmb = str(input("Nombre Del Trabajador: "))


#-----------------------categoria-->
print ("\ncategorias de trabajadores")
print ("a.Novato - b.Experto - c.Supervisor - d.Administrativo")
segi2 = True
while segi2:
    cat = str(input("Categoria: ")).strip()
    if cat == "b" or cat == "B":
        bono = 50000
        segi2 = False
    elif cat == "a" or cat == "A" or cat == "c" or cat == "C" or cat == "d" or cat == "D":
        cat = ""
        bono = 0
        segi2 = False
    else:
        print ("Las opciones validas son solo a,b,c,d")
        segi2 = True
    #--------------------------------------fin categoria-->
        
#----------------dias ausentes----------------------------->
segi3 = True
while segi3:
    dif = input("Dias ausencia: ").strip()
    if dif.isdigit() == False:
        print ("Ingrese un numero entre 0 y 30")
        sigi3 = True 
        
    elif int(dif) >= 1 and int(dif) <= 30:
        segi3 = False
        bono2 = 0
    elif int(dif) == 0:
        bono2 = 50000
        segi3 = False
    else:
        print ("Ingrese un numero entre 0 y 30")
        segi3 = True
    #-------------------------------------------------->

#--------------------afp------------------------------>
afp = str(input("Ingrese sistema de afp: "))
print ("descuento por AFP es 10% del sueldo bruto")
    #-------------------------------------------------->

#-------------------------salud------------------------->
segi6 = True
while segi6:
    sal = str(input("Sistema de salud: ")).strip()
    if str(sal) == "a" or str(sal) == "A":
        sal = "a"
        segi6 = False
    elif str(sal) == "b" or str(sal) ==  "B":
        sal = "b"
        segi6 = False
    elif str(sal) == "c" or str(sal) ==  "C":
        sal = "c"
        segi6 = False
    else:
        print ("solo se puede ingresar a,b,c")
        segi6 = True
#-------------------------------------------------->

#------------------------sueldo bruto-------------------------->
segi7 = True
while segi7:
    sld = input("Monto Sueldo Bruto: $").strip()
    if sld.isdigit() == False:
        print ("solo puede ingresar numeros")
        sigi3 = True
    elif int(sld) < 1:
        print ("el monto no puede ser negativo")
        sigi3 = True
    else:
        segi7 = False
#-------------------------------------------------->

#-------------------------------------------------->
#descuento distintos sys salud------------------------>
sld = (int(bono) + int(bono2))+int(sld)

print ("monto Bono",sld)
#----------------calculo sueldo liquido--------------------->
#descuento afp
afps = int(sld) * 0.1
       
if str(sal) == "a":
    sala1 = int(sld) * 0.057
elif str(sal) == "b":
    sala1 = int(sld) * 0.061
elif str(sal) == "c":
    sala1 = int(sld) * 0.065


    
desct = int(sld) - (int(sala1) + int(afps))

    
#si no falto niun dia +50mil
difp = 50000
#si categoria es experto el bono es doble
catp = 100000
    
    

#---------------imprimir resultados------------>
print ("Fecha: ",mes,"/",int(ano))
print ("Nombre: ",nmb)
print ("Rut: ",rut)
print ("Descuento de salud: ",sala1)
print ("Descuento por AFP: ",afp," ",afps)
print ("Dias ausencias: ",dif)
print ("Sueldo liquido: ",desct)
    """

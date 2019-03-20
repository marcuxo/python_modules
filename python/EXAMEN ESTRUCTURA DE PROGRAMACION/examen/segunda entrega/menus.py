import calculo
import datetime

x = datetime.datetime.now()
#--listas de ingresos de datos\/
MONTH = []
YEAR = []
RUT = []
NAME = []
KTGORY = []
DAYFALS = []
AFP = []
HEALT = []
#--listas para calculo de sueldo\/
SLDB = []
GIFT = []
DCTOAFP = []
DCTOHEALT = []
def controlacces(usr,pasw):
    paser = ["user","admin123"]
    
    if usr == paser[0]:
        dat = False
        if pasw == paser[1]:
            dat = False
        else:
            print ("\nel usuario o la contraseña son incorrectos")
            dat = True
    else:
        print ("\nel usuario o la contraseña son incorrectos")
        dat = True

    return dat

def menu():

    print ("\na. Ingresar datos")
    print ("b. Calcular sueldo")
    print ("c. Listar Empleados")
    print ("d. Mostrar liquidaciones por Rut")
    


    segi1 = True
    while segi1:
        opcn = input("Elija la opcion a realizar: ").strip()
        
        if opcn == "a" or opcn == "A":
            datos()
            segi1 = False
        elif opcn == "b" or opcn == "B":
            if len(SLDB) <= int("0"):
                print ("Para calcular el Sueldo es necesario ingresar los datos primero")
                segi1 = True
            else:
                print ("")
                calculo.calculoSLD(MONTH,YEAR,RUT,NAME,KTGORY,DAYFALS,AFP,HEALT,SLDB,GIFT,DCTOAFP,DCTOHEALT)
                segi1 = False
            
        elif opcn == "c" or opcn == "C":
            if len(SLDB) <= int("0"):
                print ("para mostrar los nombres, primero debe ingresar los datos")
                segi1 = True
            else:
                print ("")
                calculo.listanombres(NAME)
                segi1 = False
        elif opcn == "d" or opcn == "D":
            cion = "d"
            segi1 = True
        else:
            print ("Las opciones validas solo son a,b,c,d")
            segi1 = True
def datos():
#<---------------ingreso de datos--------------------->
    segi4 = True
    while segi4:
        a = str(input("\ningrese mes: "))
        mes = a.lower()
        meses = ("enero","febrero","marzo","abril","mayo","junio","julio",
             "agosto","septiembre","octubre","noviembre","diciembre")
        if mes in meses:
            segi4 = False
        else:
            print ("ingrese un mes valido")
    MONTH.append(mes)

    
    segi5 = True
    minm = 1950
    while segi5:
        ano = input("\nIngrese el año: ").strip()
        if ano.isdigit() == False:
            print ("el año no puede ser mayor al año actual. ",x.year)
            segi5 = True
            
        elif int(ano) < int(minm) or int(ano) > int(x.year):
            print ("el año no puede ser mayor al año actual. ",x.year)
            segi5 = True
        else:
            segi5 = False
    YEAR.append(ano)


    segi8 = True
    while segi8:
        print ("\nEjemplo de rut; 12345678-9")
        rut = input("Rut del Trabajador: ")
        if rut.isdigit() == True:
            print ("Ingrese un rut valido.")
        elif len(rut) < 11:
                if rut[8] == str("-"):
                     RUT.append(rut)
                     segi8 = False
                else:
                    print ("Ingrese un rut valido.")
        else:
            print ("Ingrese un rut valido.")

            
    segi10 = True
    while segi10:
        nmb = str(input("\nNombre Del Trabajador: "))
        if nmb.isdigit() == True:
            print ("ingrese un nombre valido")
            segi10 = True
        elif len(nmb) <= int("4"):
            print ("ingrese un nombre valido")
            segi10 = True
        else:
            NAME.append(nmb)
            segi10 = False

            
    print ("\ncategorias de trabajadores")
    print ("a.Novato - b.Experto - c.Supervisor - d.Administrativo")
    segi2 = True
    while segi2:
        cat = str(input("Categoria: ")).strip()
        if cat == "b" or cat == "B":
            cat = ("Experto")
            bono = True
            segi2 = False
        elif cat == "a" or cat == "A" or cat == "c" or cat == "C" or cat == "d" or cat == "D":
            cat = cat.lower()
            if cat == str("a"):
                cat = ("Novato")
            elif cat == str("c"):
                cat = ("Supervisor")
            elif cat == str("d"):
                cat = ("Administrativo")
            bono = False
            segi2 = False
        else:
            print ("Las opciones validas son solo a,b,c,d")
            segi2 = True
    KTGORY.append(cat)


    
    segi3 = True
    while segi3:
        dif = input("\nDias ausencia: ").strip()
        if dif.isdigit() == False:
            print ("Ingrese un numero entre 0 y 30")
            sigi3 = True 
            
        elif int(dif) >= 1 and int(dif) <= 30:
            segi3 = False
            bono2 = False
        elif int(dif) == 0:
            bono2 = True
            segi3 = False
        else:
            print ("Ingrese un numero entre 0 y 30")
            segi3 = True
    DAYFALS.append(dif)



    segi11 = True
    while segi11:
        afp1 = str(input("\nIngrese AFP: "))
        if afp1.isdigit() == True:
            print ("ingrese un nombre valido")
            segi11 = True
        else:
            AFP.append(afp1)
            segi11 = False


            
    segi6 = True
    print ("\nTramos de salud: a, b, c")
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
    HEALT.append(sal)




    segi7 = True
    while segi7:
        sld = input("\nMonto Sueldo Bruto: $").strip()
        if sld.isdigit() == False:
            print ("solo puede ingresar numeros")
            sigi3 = True
        elif int(sld) < 1:
            print ("el monto no puede ser negativo")
            sigi3 = True
        else:
            segi7 = False
    SLDB.append(int(sld))#0
    
    #bono
    if bono == True and bono2 == True:
        bonos = int("100000")
    elif bono2 == True:
        bonos = int("50000")
    else:
        bonos = int("0")
    GIFT.append(bonos)#1
    
    #descuento afp
    afps = int(sld) * 0.1
    DCTOAFP.append(afps)#2
    
    #descuento salud
    if str(sal) == "a":
        sala1 = int(sld) * 0.057
    elif str(sal) == "b":
        sala1 = int(sld) * 0.061
    elif str(sal) == "c":
        sala1 = int(sld) * 0.065

    DCTOHEALT.append(sala1)#3
    menu()
   

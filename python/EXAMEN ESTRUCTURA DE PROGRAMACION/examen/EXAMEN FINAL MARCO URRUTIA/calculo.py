import menus
def calculoSLD(MONTH,YEAR,RUT,NAME,KTGORY,DAYFALS,AFP,HEALT,SLDB,GIFT,DCTOAFP,DCTOHEALT):
    for z in range(len(SLDB)):
        print ("\n")
        suma1 = SLDB[z] + GIFT[z]
        suma2 = DCTOAFP[z] + DCTOHEALT[z]
        sldliq = int(suma1) - int(suma2)
        if int(GIFT[z]) > int("0"):
            bono = ("Tiene Bono")
        else:
            bono = ("No Tiene Bono")
        
        print ("Rut:",RUT[z])
        print ("Nombre:",NAME[z].title())
        print ("Bono:$",GIFT[z])
        print ("Descuento APF:$",int(DCTOAFP[z]) ,"Descuento de salud:$",int(DCTOHEALT[z]))
        print ("Sueldo bruto $",SLDB[z])
        print ("Total a pagar:$",sldliq)
    menus.menu()
    
    
def listanombres(NAME):
    NOMBRES = []
    for x in NAME:
       if x not in NOMBRES:
           NOMBRES.append(x)
    nombres = tuple(NOMBRES)
    print (nombres)
    menus.menu()
    
def cargas(rut):
    cargas = {"rut":rut}
    #print (cargas)
    #print (rut[2])
    print ("""Para ingresar cargas busquelo por el rut
    -EJ: 161234561
    """)
    segir = True
    while segir:
        ruts = input("Ingrese rut: ").strip()
        if ruts.isdigit() == False:
            print ("rut ingresado no existe")
            segir = True
        elif int(ruts) in rut:
            dato = int(input("INGRESA CARGAS: "))
            rut.append(dato)
            dato = str(input("ingrese estado civil: "))
            rut.append(dato)
            segir = False
        else:
            print ("rut ingresado no existe")
            segir = True
        
            

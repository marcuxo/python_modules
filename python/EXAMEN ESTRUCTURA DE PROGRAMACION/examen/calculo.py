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

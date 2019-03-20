"""
LOGO = ""
MONTH="enero"
YEAR=2017
RUT="16114499-1"
NAME="marco urrutia molina"
KTGORY="experto"
DAYFALS=10
AFP="cuprum"
HEALT="b"
SLDB=500000
GIFT=100000
DCTOAFP=10000

DCTOHEALT=12000
SUMA1 = SLDB+GIFT
DIAS = int(SUMA1/30)
DCTODAYS = DIAS*DAYFALS
DCTO = (DCTOAFP+DCTOHEALT+DCTODAYS)
SLDOLIQ = SUMA1-DCTO
print ("-----------------LIQUIDACION SUELDO--------NovaVision s.a\n")
print ("  Rut:",RUT,"\t\tFecha:",MONTH,"/",YEAR)
print ("  Nombre:",NAME)
print ("  Categoria Trabajador:",KTGORY,"    Dias ausentes:",DAYFALS)
print ("  AFP:",AFP,"\tTramo de Salud:",HEALT)
print ("----------------------------------------------------------")
print ("  Sueldo Bruto....................................",SLDB)
print ("  Bono Asistencia + categoria.....................",GIFT)
print ("----------------------------------------------------------")
print ("  Total Imponible.................................",SUMA1)
print ("---------------------------------------------------------")
print ("  Dias Ausentes(",DAYFALS,").............................",DCTODAYS)
print ("  Descuento AFP...................................",DCTOAFP)
print ("  Descuanto Salud.................................",DCTOHEALT)
print ("----------------------------------------------------------")
print ("  Total descuentos................................",DCTO)
print ("==========================================================")
print ("  Sueldo liquido..................................",SLDOLIQ)
print ("\n")
print ("\n")
print ("\t____________________________")
print ("\t    ",NAME,".")
print ("\n")
print ("\n")


NAME = ["marco","juan","marco","diego"]
NOMBRES = []


for x in NAME:
    if x not in NOMBRES:
        NOMBRES.append(x)
nombres = tuple(NOMBRES)
print (nombres)


import ctypes
name = "Marco"
msg = ("Hasta luego "+ name)
a = ctypes.windll.user32.MessageBoxW(0, msg, "NovaVision",4)
if int(a) == 6:
    print ("si")
else:
    print ("no")

"""
#busca pociciones
name = [1,2,3,1,1,1,1,1,1,1,13,2,1]
find = []
buscar = int(input("que buscas: "))
for i,x in enumerate(name):
    if x == buscar:
        find.append(i)
print (find)

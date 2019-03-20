lista = [1,2,3,"marco",5,6,7,8,9,10,
         11,12,13,"juan",15,16,14,18,19,10,
         21,22,23,"andres",25,26,27,28,29,10]
"""
dive = (len(lista))
div = int(dive)+1
#x = 0
for a in range(3,div,10):
    print ("Nombre: ",lista[a])
    #print ("--------------")
    #x = x + 10
    #for r in range(a,x):
        #if r >= len(lista):
           # x = len(lista)
        #else:
           # print (lista[r])
"""

RUT = [16114499-0,16114499-1,16114499-0,16114499-3,16114499-4]
NAME = ["MARCO U","AGUSTIN","ELSA","ESCARLET","ANAIS"]


rutes = []
import re
for a in range(0,3):
    cadena = input("ingresa rut: ")
    cadena = re.sub("\D", "", cadena)
    rutes.append(cadena)
print (rutes)




buscar = input("que buscas:")
busqueda=[i for i,x in enumerate(rutes) if x == buscar]
print (busqueda)
for i in busqueda:
    print ("Rut: ",rutes[i])
    print ("Nombre: ",NAME[i])
 
"""      
def listanombres(NAME):
    NOMBRES = []
    for n in NAME:
        #x = NAME[n]
        NOMBRES.append(n)
    print ("lista: ",NOMBRES)
    nombres = tuple(NOMBRES)
    print ("TUPLA: ",nombres)
dato = ["marco","Elsa","Agustin","Escarlet","Anais"]
listanombres(dato)
"""        
#RUT = [16114499-0,16114499-1,16114499-0,16114499-3,16114499-4]
#NAME = ["MARCO U","AGUSTIN","ELSA","ESCARLET","ANAIS"]



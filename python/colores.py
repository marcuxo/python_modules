#-----------imprime solo alguans cosas-------------->
lista = [1,2,3,"marco",5,6,7,8,9,10,
         11,12,13,"elsa",15,16,14,18,19,10,
         21,22,23,"agustin",25,26,27,28,29,10,
         31,32,33,"escarlet",35,36,37,38,39,10,
         41,42,43,"anais",45,46,47,48,49,10]

dive = (len(lista))+1
for a in range(3,dive,10):
    print ("Nombre: ",lista[a].title())
#----------------------busca e imprime---------------------->
segi22 = True
while segi22:
    buscar = input("que buscas:")
    if buscar.isdigit() == True:
        if len(buscar) <= int("0"):
            segi22 = True
        else:
            segi22 = False
busqueda=[i for i,x in enumerate(lista) if x==int(buscar)]
print (busqueda)
for i in busqueda:
    print (lista[i])
    
#----------------convercion---------------------------->   
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
        




def c(a, b):
    print (a)
    print (b)
    

























"""
datasheet =[]
segi8 = True
while segi8:
    print ("\nEjemplo de rut; 12345678-9")
    rut = input("Rut del Trabajador: ")
    if rut.isdigit() == True:
        print ("Ingrese un rut valido.")
    elif len(rut) < 11:
            if rut[8] == str("-"):
                 datasheet.append(rut)
                 segi8 = False
            else:
                print ("Ingrese un rut valido.")
    else:
        print ("Ingrese un rut valido.")




segi10 = True
while segi10:
    nmb = str(input("Nombre Del Trabajador: "))
    if nmb.isdigit() == True:
        print ("ingrese un nombre valido")
        segi10 = True
    elif len(nmb) <= int("3"):
        print ("ingrese un nombre valido")
        segi10 = True
    else:
        datasheet.append(nmb)
        segi10 = False
print (datasheet)

for i in range(len(datasheet)):
    print (datasheet[i])

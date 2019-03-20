paser = []
alumno1 = [paser,]
user = input("ingresa user: ")
paser.append(user)

segi = True
while segi:
    pas0 = input("Ingrese password: ")
    pas1 = input("Confirme password: ")
    if pas0 == pas1:
        print ("Password confirmado")
        paser.append(pas0)
        segi = False
    else:
        print ("Los passwords con coinciden")
        segi = True

print (alumno1[0:1])
print ("\t\nAcceso al softward")
segi0 = True
while segi0:
    usr = input("Ingrese su usuario: ")
    if usr == alumno1[0][0]:
        segi1 = True
        while segi1:
            pasw = input("Ingrese su pasword :")
            if pasw == alumno1[0][1]:
                print ("bienvenido", usr)
                segi1 = False
                segi0 = False
            else:
                print ("Password incorrecto")


def ax():
    print("\t Bienvenido")
    a1=['Nombre: Daniel Guerrero','Rut: 17579130-2','e-mail: Dguerrero@gmail.com']
    a2=["Nombre: Felipe Díaz","Rut: 16322614-5","e-mail: Fdiaz@gmail.com"]
    a3=["Nombre: José Marín","Rut: 17775316-6","e-mail:  Jmp@gmail.com"]
    a4=["Nombre: Javier Leiva","Rut:11362331-1","e-mail: Jleiva@gmail.com"]
    ide={'ide1':a1,"ide2":a2,"ide3":a3, "ide4":a4}

    seguir=True
    while(seguir):
        i= input("Ingrese Clave:")
        if (i in ide):
            print(ide[i][0])
            print(ide[i][2])
            print(ide[i][1])
            print("")
        else:
            print("La Clave No Esta Registrada En La Base De Datos.")
            seguir=True
ax()

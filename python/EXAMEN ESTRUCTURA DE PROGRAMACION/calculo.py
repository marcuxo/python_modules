def calculoSLD(sld, datos):
    if len(sld) <int("0"):
        print ("Para calcular el Sueldo es necesario ingresar los datos primero")
        menus.menu()
    else:
        print ("")
        
    print ("Aca se calcula el sueldo")
    sueldoLiquido = (sld[0]+sld[1])-(sld[2]+sld[3])
    print ("el sueldo liquido a pagar es:$",sueldoLiquido)
    print (sld)
    
    return

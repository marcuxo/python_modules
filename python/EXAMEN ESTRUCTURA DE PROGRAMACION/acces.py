def controlacces(usr, pasw):
    paser = ["user","admin123"]
    
    if usr == paser[0]:
        dat = False
        if pasw == paser[1]:
            print ("bienvenido")
            dat = False
        else:
            print ("\nel usuario o la contraseña son incorrectos")
            dat = True
    else:
        print ("\nel usuario o la contraseña son incorrectos")
        dat = True

    return dat


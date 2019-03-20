marco = ['user','pasword']
print (marco)

dat = True
while dat:
    user = input('ingrese Usuario=>')
    if marco[0] == user:
        #print ('bienvenido')
        dat = False
    else:
        print ('usuario incorrecto')
        dat = True
    dat2 = True
while dat2:
    pasw = input('Ingrese password=>')
    if marco[1] == pasw:
            
        dat2 = False
    else:
        print ('password incorrecto')
        dat2 = True
print ('\n\tBienvenido')
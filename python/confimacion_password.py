lis = []
print ('\tSu nombre sera su usuario ')
print ('\tpara iniciar sesion')
usr = str(input('ingrese su nombre =>'))
lis.append(usr)
dat = True
while dat:
    pasw1 = input('ingrese pasword=>')
    pasw2 = input('confirme pasword=>')
    if pasw1 == pasw2:
        print ('pasword correcto')
        lis.append(pasw1)
        dat = False
    else:
        print ('los pasword no coinciden')
        dat = True

print (lis)
isr2 = input('ingresa usuario')
if isr2 in lis:
    past = input('ingrese password')
  
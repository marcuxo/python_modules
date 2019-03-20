"""import re
 
n = input("Digite letra ")
 
if n == n.lower():
    if re.match("(a|e|i|o|u)",n):
        print ("Es minuscula y vocal")
    else:
        print("es minuscula y consonante")
if n == n.upper():
    if re.match("(A|E|I|O|U)",n):
        print("Es mayuscula y vocal")
    else:
        print("Es mayuscula y consonante")
"""
a = str(input("ingrese mes: "))
b = a.lower()
meses = ("enero","febrero","marzo","abril","mayo","junio","julio",
         "agosto","septiembre","octubre","noviembre","diciembre")
if b in meses:
    print (b)
else:
    print ("ingrese un mes valido")

#import os
import platform
def asco(lis1,lis2):
    ind = 0
    for i in lis1:
        for a in lis2:
            if i == a:
                print (a,i)


a = [1,2,3,7]
b = [4,5,6,7,3]
asco(a,b)

print (platform.python_version())
#print ("Descripcion:", platform.uname())

print
print ('Sistema   :', platform.system())
print ('Red       :', platform.node())
print ('Version   :', platform.version())
print ('Tipo      :', platform.machine())
print ('Procesador:', platform.processor())

#os.system("cls")
print ("--------------------------------- ")
win = "Windows"
if platform.system() == win:
    print ("True: ",win)
else:
    print ("False: ",platform.system())



import random
import string
for a in range (1,100):
    password = "".join(random.choice(string.ascii_uppercase + string.digits) for x in range(12))
    print (a,password)

# JUEGO PICAS Y PALAS

from random import randint #importa solo una funcion de esta libreria

lista=[]

for i in range(10):

    n=randint(0,9)
   
    if n in lista:
        print("num rep")
    else:
        lista.append(n)
    if len(lista)==3:
        break

print(lista)

    
    

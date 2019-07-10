from random import randint #importa solo una funcion de esta libreria

n=randint(0, 100)
print(n)
adivinado=False

for i in range(5):
    a=int(input("ingrese su valor: "))
    print(a)
    if a<n:
        print("el numero a adivinar es mayor")
    elif a>n:                                   #con este comando ya no se hacen las dos preguntas
        print("el numero a adivinar es menor")
    else:  # no requiere ninguna condicion
        print("ganaste")
        adivinado = True
        
        break    #sentencia de salto para salir del ciclo for      

if not adivinado:
    print("el numero aleatorio fue: " + str(n))
    
        

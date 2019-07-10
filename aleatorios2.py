from random import randint #importa solo una funcion de esta libreria

n=randint(0, 100)
print(n)

for i in range(5):
    a=int(input("ingrese su valor: "))
    print(a)
    if a<n:
        print("el numero a adivinar es mayor")
    if a>n:
        print("el numero a adivinar es menor")
    if a==n:
        print("ganaste")
        break    #sentencia de salto para salir del ciclo for      

        

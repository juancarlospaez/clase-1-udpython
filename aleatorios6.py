# ahora con tres numeros aleatorios


from random import randint #importa solo una funcion de esta libreria

lista=[]
for i in range(3):
    lista.append(randint(0,100))

print(lista)
    
n=randint(0, 100)
print(n)
adivinado=False

for i in range(5):
    a=int(input("ingrese su valor: "))
    print(a)
'''   tres comillas sencillas para hacer comentarios



    if a in lista:
        print("ganaste")
        adivinado = True
        break    #sentencia de salto para salir del ciclo for      
    else:
        print("sigue intentando")
'''



if not adivinado:
    cad=""
    for i in lista:
        cad +=str(i)+", "
    print("los numeros alatorios fueron: " + cad[:-2])
    
        

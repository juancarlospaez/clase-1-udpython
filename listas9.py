valores = range(50, 101, 2) # se genera de 50 a 101 pero de 2 en dos

print (list(valores)) #para mostrar una lista de lo contrario mostraria solamente el rango

n=0
m=0
for i in valores:   #se define un bloque de codigo, luego de este blloque de codigo todo debe estar identado
    if i%2 == 0: #el igual de comparacion es == diferente al = de asignacion
        n=n+i           # despues de los dos puntos todo el codigo debe estar identado
    else:
        m=m+i
print("suma de numeros pares  " + str(n))
print("suma de numeros impares   " + str(m))


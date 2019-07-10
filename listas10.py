#ejercicioconsiste en escribir los cuadrados de los primeros 100 numeros

valores = range(101) 

print (list(valores)) #para mostrar una lista de lo contrario mostraria solamente el rango

n=0
m=0
for i in valores:   #se define un bloque de codigo, luego de este blloque de codigo todo debe estar identado

    n=i**2
    print("cuadrado de  "+ str(i)+" es: " + str(n))


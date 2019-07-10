#ejercicioconsiste en escribir los cuadrados de los primeros 100 numeros
#el mismo resultado pero metido dentro de una lista
#listas por comprension

valores = [x**2 for x in range(5,101,5)] # para los multiplos de 5

print(len(valores)) #cuenta el numero de elementos de la lista

print(sum(valores)) #suma todos los valores de la lista

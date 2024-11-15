
import numpy as np
lista = [[2, 3, 7],
        [4, 1, 3],
        [3, 4, 5]]

n1 = np.array(lista) #las listas pueden ser detodo contodo y los array nomas seran de un solo tipo

print(n1)
print(n1.ndim) #numero de dimenciones  hasta N
print(n1.shape) #me esta regresando una tupla como tama;o de mis dimenciones
print(n1.size) #cuenta los elementos
print(n1.dtype) #tipo de dato

numeros = np.array([2, 4, 6, 8, 10, 12, 14])
print(numeros*2) #estas operaciones se pueden hacer mas rapidas con estos comandos o sea ahorrarte ciclos
print(numeros.cumsum()) #esto seria hacer una suma acumulada o sea 2 mas 4 y mas 8

print(numeros[4]) #es para agarrar o cambiar el numero de la posicion puesta en el print
print(n1[1, 3]) #el 1 es la columna y el numero 3 es para agarrar la posicion deseada en este caso de la lista

filtros = numeros % 2 == 0
print(numeros[filtros]) #se usa para filtrar numeros mas rapidos sin usar ciclos

"""
ECUACIONES
X + 2Y = 1
3X + 5Y = 2
"""
ecuaciones = np.array([[1, 2], [3, 5]])
resultados = np.array([1, 2])
print(np.linalg.solve(ecuaciones, resultados))



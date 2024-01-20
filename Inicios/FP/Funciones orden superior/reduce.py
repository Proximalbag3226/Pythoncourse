#la funcion reduce se podria decir que es un tipo de funcion acumulativa para los elementos de una lista, bastante util a la hora de hacer sumatorias
#Por cierto la funcion reduce se tiene que importar desde functools
#Ejemplo
from functools import reduce
numeros = [1, 2, 3, 4, 5]
total = reduce(lambda x,y:x+y, numeros)
print(total)

#Y si lo hacemos con una funcion normal

def sumar(num1, num2):
    return num1 + num2
total2 = reduce(sumar, numeros)
print(total2)
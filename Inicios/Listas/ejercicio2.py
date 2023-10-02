#Escriba un programa que contenga las siguientes listas y que a continuacion cree las siguientes listas (en las que no debe haber repeticiones):
#Lista de elementos que aparecen en las dos listas
#Lista de elementos que aparecen en la primera pero no en la segunda
#Lista de elementos que aparecen en la segunda pero no en la primera
#Lista de elementos que aparecen en ambas

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#eliminamos los elementos repetidos al pasar las listas a conjuntos
a = set(lista1)
b = set(lista2)
print(a)
print(b)

#Imprimimos los elementos de ambos conjuntos al combinarlos
c = a | b
print(c)

#Los elementos que aparecen en la primera pero no en la segunda
d =  a - b
print(d)

#los elementos que aparecen en la segunda pero no en la primera
e = b - a
print(e)

#los elementos que aparecen en ambas listas
f = a & b 
print(f)
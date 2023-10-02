#Escribe un programa donde se tenga una lista y que se eliminen los elemetos repetidos de dicha lista para posteriormente mostrar la lista

lista = [1,2,3,4,5,6,"Hola Luis",2,3,4]
print(lista)

#Para eliminar los duplicados podriamos pasar la lista a conjunto
conjunto = set(lista)
print(conjunto)

#Y la volvemos a la normalidad
lista2 = list(conjunto)
print(lista2)
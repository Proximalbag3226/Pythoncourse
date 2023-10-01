#tuplas, las tuplas son otro tipo de coleccion al igual que las listas solamente que las tuplas son inmutables, no se pueden modificar

tupla1 = (4, "hola", 6.78, [1,2,3,4],4)

print(tupla1)

#de las pocas cosas que se pueden hacer con la tupla es mostar sus elemtos 
print(tupla1[1])
print(tupla1[-1])
print(tupla1.index("hola"))
print(tupla1.count(4))
print(len(tupla1))

#tambien podemos transformar las tuplas en listas y listas en tuplas
tupla2 = (1,2,3,"hola",)
lista1 = list(tupla2)
print(lista1)

#y de regreso
tupla3 = tuple(lista1)
print(tupla3)
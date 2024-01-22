#Zip es utilzado en los bucles ya que nos permite juntar diferentes fuentes de informacion que sean iterables y se colocan en una sola estructura de datos
#Esta estructura con los diferentes iterables van a compoartir el mismo indice 

#Crearemos unas listas para poder identificar mejor 
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = ["a","b","c","d","e"]

#Vamos a combinar las listas 
for a,b in zip(lista1, lista2):
    
    #Como podremos ver ambas listas estan combinadas sus elementos compartiendo los indices 
    print(a,b)

#Ahora lo haremos con multiples elementos 
for a,b,c in zip(lista1, lista2, lista3):
    print(a,b,c)
    
#Cabe aclarar que zip no nos regresa una lista de listas si no mas bien un objeto de tipo zip que es iterable y que contiene tuplas
print(zip(lista1,lista2,lista3))

#Vamos a iterar el objeto zip en un bucle
for i in zip(lista1, lista2, lista3):
    
    #Esto a diferencia de las anteriores impresiones es que nos retorna tuplas con las listas combinadas dentro 
    print(i)

#Podemos pasarlo a lista de tuplas 
lista4 = list(zip(lista1, lista2, lista3))
print(lista4)

#Con los terminos correctos de combinacion de dos listas podemos pasarlo a diccionario
lista5 = dict(zip(lista1, lista3))
print(lista5)
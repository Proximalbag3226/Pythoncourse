#Las listas en python se pueden comparar con los arrays en otros lenguajes de prograacion
lista = ["Lunes", "Martes", "Miercoles", "Juevez", "Viernes"]

#podemos imprimir sus valores dependiendo de el valor que especifiquemos a la lista con el indice, recordando que se  empieza por el elemento 0
print(lista[2])

#y tambien podemos recorrer de final a principio, iniciando por -1
print(lista[-2])

#sublistas, imprime los valores que se el especifica restando un valor al especificado, en este caso hasta el 2
print(lista[0:3])

#tambien podemos hacerlo asi
print(lista[:3])

#para nuestra fortuna o desgracia las listas en python pueden almacenar mas de un tipo de variable o incluso listas dentro de ellas mismas
lista2 = ["Lunes", "Martes", "Miercoles", 40, 51.5, [1, 2, 3], True]
print(lista2)

#para conocer el "largo" de una lista se utiliza el metodo len
print(len(lista2))

#insertando elementos en la lista utilizando el metodo append, este metodo agrega elementos al final de la lista 
lista3 = ["Hola", 1, 2, "Mundo"]
lista3.append(6)
lista3.append("Luis")
print(lista3)

#tambien podemos agregar valores utilizando el metodo insert, se le pasan dos atributos, el primero el indice y de segundo el valor 
lista3.insert(2, "Hola2")
print(lista3)

#tambien esta el metodo  extend, donde se le pasa una lista para concatenar una lista con la otra agregando dichos elemtos al final de la otra
lista4 = [1,2,3,4]
lista4.extend([5,6,7,8])
print(lista4)

#sumar dos listas
lista5 = [1,2,3]
lista6 = [4,5,6]
lista7 = lista5 + lista
print(lista7)

#buscar valores en las listas
lista8 = [1,2,3,4,5,"Luis",1]
print(3 in lista8)
print(10 in lista8)

#para saber el numero de indice en el que se encuentra
print(lista8.index("Luis"))

#Para poder contar elementos repetidos o contar las veces que se repite en una lista
print(lista8.count(1))

#Para eliminar valores de una lista
lista9 = [1,2,3,4,5,6,7,8,9,10]

#Elimina el ultimo valor de la lista
lista9.pop()
print(lista9)

#si le pasamos un valor elimina lo que haya en ese indice
lista9.pop(2)
print(lista9)

#Se le pasa el valor que queremos elminar 
lista9.remove(6)
print(lista9)

#Para eliminar toda la lista
lista9.clear()
print(lista9)

#Voltear la lista
lista8.reverse()

#multiplicar una lista por n
lista10 = [1,2,3,4,5,"Luis"]*2
print(lista10)

#ordenar lista mayor a menor 
lista11 = [1,5,7,12,3,8,4,6]
lista11.sort()
print(lista11)

#ordenar lista de menor a mayor
lista11.sort(reverse=True)
print(lista11)

#Aqui una peque;a actualizacion a las listas, las listas por comprension, estas listas mas que ser una lista diferente a las que conocemos de toda la vida
#Son mas bien un metodo de creacion de listas para que el codigo sea mas conciso y comprensible, aqui un ejemplo de su sintaxis basica
#nueva_lista = [expresion for elemento in secuencia if condicion]
#Y aqui un ejemplo funcional 
cuadrados = [x**2 for x in range(5)]
#expresion: Es la expresión que se evalúa y se utiliza para construir cada elemento de la nueva lista.
#elemento: Es una variable que toma cada valor de la secuencia.
#secuencia: Es la secuencia de elementos sobre la cual se itera.
#condicion (opcional): Es una condición que filtra los elementos de la secuencia. Solo los elementos que cumplen la condición se incluyen en la nueva lista.
#Y tambien podemos incluir una condicion para filtrar
numeros_pares = [x for x in range(10) if x % 2 == 0]






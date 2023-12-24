#Bucle for, a diferencia de su hermano, el bucle while, el bucle for ya contiene el numero determinado de iteraciones a relizar definidas por una variable

for i in[1,2,3,4,5]:
    print("Hola mundo")
#En este caso el bucle for con su variable iteradora (i) recorre la coleccion por eso imprime hola mundo 5 veces, lo que analiza el for no es el tipo de elementos
#Si no mas bien la cantidad de elementos

for i in[1,2,3, "Luis", 3.1416]:
    print(f"El elemento es: {i}")

#ahora con un diccionario 
diccionario = {"Luis":17, "Maria":18, "Fernanda":19, "Jose":21}
for i in diccionario:
    print(f"Las claves del diccionario son: {i}")
    #Y si queremos que nos retone el valor
    print(f"El valor es: {diccionario[i]}")
    #Y si queremos los dos
    print(f"{i} -> {diccionario[i]}")

#y de manera mas "elegante"
for clave, valor in diccionario.items():
    print(f"{clave} -> {valor}")

#Con el bucle for podemos recorrer las diferentes tipos de listas y tambien cadenas

cadena = "Luis"
print(type(cadena))
for i in cadena:
    print(f"Hola {cadena}")

#tambien podemos imprimir elemento por elemento
for i in cadena:
    print(f"{i}")

#Para quitar el salto de linea y ademas que esten separados
for i in cadena:
    print(f"{i}", end=" ")

#Tambien podemos especificar la cantidad de iteraciones con un "range"
for i in range(5):
    print("Hola")

#Tenemos tambien la funcion eumerate
lista_nombres = ["Luis", "David", "Fernanda"]
for indice, valor in enumerate(lista_nombres):
    print(indice, valor)
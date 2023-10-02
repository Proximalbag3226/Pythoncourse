#Pilas, las pilas no son como tal unas estructuras de datos definidas en python pero podemos imitarlas con listas
pila = [1,2,3]
print(pila)

#podemos imitar el comportamiento agregando elementos al final de la lista
pila.append(4)
pila.append(5)
print(pila)

#tambien podemos sacar elementos asi como en una pila sacando el ultimo elemento en entrar, en este caso el 5
n = pila.pop()
print(n)

#tambien se puede hacer asi 
print(pila.pop())

#imitamos el funcionamiento de las listas de tipo lifo

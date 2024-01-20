#conjuntos, es un tipo  de coleccion donde sus elementos se agregan de forma desoordenada

#tenemos que definirlos primero con el set, ya que si no se declara como  diccionario
conjunto1 = set()
conjunto1 = {1,2,3,4, "hola"}
print(conjunto1)
#los conjuntos pueden alamcenar cualquier dato  a exepcion de otra coleccion o valores duplicados 

#para agregar elementos a un conjunto usamos el metodo add
conjunto1.add(5)
print(conjunto1)

#al agregar elementos al cojunto este mismo se agregara donde sea 
conjunto1.add("adios")
conjunto1.add(8)
conjunto1.add(5.78)
print(conjunto1)

#y para eliminar elemtos del conjunto utilizamos el metodo discard
conjunto1.discard("hola")
conjunto1.discard("adios")
print(conjunto1)

#y para borrar todos los elemtos del conjunto utilizamos el metodo clear

#para hacer busquedas de elementos dentro del conjunto
print(3 in conjunto1)
print(11 in conjunto1)

#o tambien lo contratio para saber si un elemto NO esta dentro de uin conjunto  
print(3 not in conjunto1)
print(11 not in conjunto1)

#ahora creemos dos conjuntos mas
conjunto2 = set()
conjunto3 = set()
conjunto2 = {1,2,3,4}
conjunto3 = {4,5,6,7}

#si queremos crear conjuntos con elementos ya definidos podemos crearlos directamente declarandolo de la manera siguiente conjuntoa = {a,b,c}

#si un conjuto tiene los mismo elementos que otro para python estos dos seran los mismos 
print(conjunto2 == conjunto3)

#tambien podemos utilizar el metodo len para mostrar la cantidad de elementos que contiene un conjunto
print(len(conjunto2))
print(len(conjunto3))

#operaciones que podemos realizar sobre los conjuntos como en probabilidad ejemplo de union 
conjunto4 = conjunto2 |	conjunto3
print(conjunto4)

#interseccion de conjuntos 
conjunto5 = conjunto2 & conjunto3
print(conjunto5)

#diferencia de conjuntos
conjunto6 = conjunto3 - conjunto2

#diferencia simetrica
conjunto7 = conjunto3 ^ conjunto2

#como podemos obvervar los conjuntos son bastante utiles a la hora de relizar operaciones que involucren problemas de probabilidad 

#a un conjunto estar contenido dentro de otro se le puede llamar subconjunto
print(conjunto2.issubset(conjunto1))
print(conjunto2.issuperset(conjunto1))

#conjuntos disxonexos o que no comparten ningun elemento en comun
print(conjunto2.isdisjoint(conjunto1))

#conjuntos inmutables asi como las tuplas 
conjunto8 = frozenset({1,2,3,4,5,6,7,8})

#Actualizacion de los conjuntos para ver los conjuntos por compresion, esta es una forma de crear conjuntos en una sola linea de codigo para facilitar 
#La escritura del codigo y su comprension, aqui su sintaxis
#nuevo_conjunto = {expresion for elemento in secuencia if condicion}
#expresion: Es la expresión que se evalúa y se utiliza para construir cada elemento del nuevo conjunto.
#elemento: Es una variable que toma cada valor de la secuencia.
#secuencia: Es la secuencia de elementos sobre la cual se itera.
#condicion (opcional): Es una condición que filtra los elementos de la secuencia. 
# Solo los elementos que cumplen la condición contribuirán a la construcción del nuevo conjunto.

#Ejemplo
cuadrados_set = {x**2 for x in range(5)}

#Filtrado de elementos>
numeros_pares_set = {x**2 for x in range(10) if x % 2 == 0}



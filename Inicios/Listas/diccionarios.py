#Diccionarios estos tienen la caracteristia de tener dos elementos por posicion, clave y valor la clave no puede estar repetida y se separan con dos puntos
diccionario1 = {"azul":"blue", "rojo":"red", "verde":"green"}
print(diccionario1)

#para imprimir un valor especifico  del diccionario tenemos que poner su clave
print(diccionario1["azul"])
print(diccionario1["rojo"])

#para agregar nuevos elementos al diccionario primero ponemos su clave y despues su valor 
diccionario1["amarillo"] = "yellow"
print(diccionario1)

#para modificar valores del diccionario
diccionario1["azul"]  = "BLUE"
print(diccionario1)

#para eliminar un valor del diccionario tenemos que poner su clave
del(diccionario1["verde"])
print(diccionario1)

#los diccionarios tambien pueden contener los diferentes tipos de valores incluidos otros diccionarios dentro de los mismos 
equipo = {10:"Paulo Divala", 11:"Douglas Costa", 7:"Cristiano Ronaldo", 17:"Mario Mandzukich"}
print(equipo)

#pasamos el valor a buscar
print(equipo[10])

#si trtamos de acceder a una clave que no existe nos regresara un error de clave
#print(equipo[6])

#pero tambien podemos especificar que mensaje nos puede retornar en caso de que no se encuentre la clave dentro del diccionario
print(equipo.get(6, "No exite un jugador con ese dorsal"))

#tambien podemos comprobar la existencia de la clave dentro del diccionario
print(11 in equipo)

#si queremos que se nos muestren las claves del diccionario lo hacemos de la siguiente manera
print(equipo.keys())

#Si al contrario queremos que se nos muestren los valores mas no las claves lo hacemos asi
print(equipo.values())

#y si queremos que se muestren ambos 
print(equipo.items())

#y si queremos la longitud del diccionario
print(len(equipo))

#y para eliminar todo el valor del diccionario
#equipo.clear()

#Peque;a actualizacion de los diccionarios, donde veremos los diccionarios por comprension, estos son una manera mas concisa y facil de construir dirccionarios
#Mas facil y legible de crear basados en iteraciones y expresiones, su sintaxis basica es la siguiente
#nuevo_diccionario = {clave: valor for elemento in secuencia if condicion}
#clave: Es la expresión que se evalúa y se utiliza como clave para cada par clave-valor en el nuevo diccionario.
#valor: Es la expresión que se evalúa y se utiliza como valor correspondiente a la clave en el nuevo diccionario.
#elemento: Es una variable que toma cada valor de la secuencia.
#secuencia: Es la secuencia de elementos sobre la cual se itera.
#condicion (opcional): Es una condición que filtra los elementos de la secuencia. Solo los elementos que cumplen la condición contribuirán a la construcción del nuevo diccionario.

#Aqui un peque;o ejemplo de su uso
cuadrados_dict = {x: x**2 for x in range(5)}

#Y aqui con una condicion de filtrado
numeros_pares_dict = {x: x**2 for x in range(10) if x % 2 == 0}



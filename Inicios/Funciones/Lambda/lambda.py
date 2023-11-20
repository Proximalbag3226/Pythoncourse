#las funciones lambda o tambien conocias como funcions de orden menor, estas funciones son mas pequeñas que las normales ya que estan diseadas para solamente 
#Ejecutarse una vez y no volver a tocarse en todo el codigo y se usa para ejecutar una tarea una unica vez 

#Creamos una funcion lambda que solamente va a ser utilzada una vez para retornar el valor 2 de la tupla estudiantes, no se declara el return ya que las 
#Funciones lambda tienen return por defecto y solamente se pasa el argumento que va a aceptar 
#lambda estudiante: estudiante[1] en el ejemplo practico vamos a utilizar la variable x para que sea mas simple 

#Vamos a ordenar la siguiente lista dependiendo de las notas usando funciones de orden superior
lista_estudiantes = [('Edward',4.2),('Pepe',2.5),('Maria',3.1),('Carlos',4.5)]

lista_ordenada = sorted(lista_estudiantes,key=lambda x:x[1])
print(lista_ordenada)

#Si quisiese hacerse el orden al reves se utiliza el argumento reverse 
lista_ordenada2 = sorted(lista_ordenada,key=lambda x:x[1], reverse=True)
print(lista_ordenada2)


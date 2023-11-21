#La funcion sorted permite ordenar los elemetos de un iterable depenediendo de la llave que se pase

#Tenemos la lista de tuplas de estudiantes
estudiante = [('Juan',22,95,'555-1234'),('Pedro',18,89,'555-5678'),('Mario',25,94,'555-9876')]

#Funcion para retornar la edad
def edad(estudiante):
    return estudiante[1]

#Utilizamos sorted pasando la lista de tuplas de estudiantes y la llave que es la funcion de la edad
lista_estudiantes_edad = list(sorted(estudiante,key=edad))
print(lista_estudiantes_edad) 

#Y ahora con lambda 
lista_estudiantes_edad2 = list(sorted(estudiante,key=lambda x:x[1]))
print(lista_estudiantes_edad2)

#Y ahora al revez
lista_estudiantes_edad3 = list(sorted(estudiante, key=lambda x:x[1], reverse=True))
print(lista_estudiantes_edad3)
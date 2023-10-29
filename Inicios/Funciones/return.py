#En este caso veremos la sentencia return que se utiliza de manera en las funciones y su uso es para poder obtner un valor obtenido de una funcion en una variable
#Si podemos ver en los ejemplos diferentes de las funciones que hemos realizado las cosas que realizan las funciones no regresan un tipo de valor solamente
#Se van directamente a la consola, pero esto solamente es un ejemplo teorico, la mayoria de las funciones realizan una accion que retorna algun valor o nada
#Ejemplo

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

resultado = suma(1,3)
print(f"El resultado es {resultado}")

resultado_final = resultado * 2
print(f"El resultado final es {resultado_final}")

#Como podemos ver la funcion no nos imprime directamente un valor si no que nos regresa ese valor almacenado en una variable para que nosotros podamos inteactuar con el 
#Tambien podemos retornar varios valores en una misma funcion para ello veremos el siguiente ejemplo con un ejemplo anterior en este miosmo capitulo de funciones
def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = (cantidad * precio_u) * (1-descuento)
    return nombre_producto, cantidad, precio_final

nombre, cantidad, precio = calcular_precio("medias", 3, 10)
print(nombre)
print(cantidad) 
print(precio)

#Como podemos obvservar la funcion ahora nos retorna  multiples valores en forma de tupla 
#Recordemos que la tupla es una forma de almacenamiento de datos donde los datos almacenados dentro de ella son inmutables y solamente podemos consularlos con su indice
#En este caso al retornarnos 3 valores y pedir dichos valores hemos desplegado los valores de la tupla en sus respectivas variables
    
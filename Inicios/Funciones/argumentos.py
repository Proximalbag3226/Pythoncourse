#Positional arguments
def imprimir_nombre(primer_nombre, 
                    segundo_nombre,
                    primer_apellido,
                    segundo_apellido):
    
    print(f"Hola {primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido} bienvenido al curso de python")
    
#Asi se establecen los argumentos posicionales para la funcion imprimir_nombre
    
imprimir_nombre("Luis", "Enrique", "Perez", "Corona")
    
#Ahora estableceremos los mismos argumentos pero de manera key
imprimir_nombre(primer_apellido="Perez", segundo_nombre="Enrique", segundo_apellido="Corona", primer_nombre="Luis")

#Tambien podemos combinar ambas formas para pasar los argumentos

imprimir_nombre("Luis", "Enrique", segundo_apellido="Corona", primer_apellido="Perez")

#Iterable umpaking, esta tambien es una forma de pasar argumentos a las funciones a travez de elementos iterables como son las tuplas, listas, conjuntos
#Lo mas comun es utilizar tuplas

#Definimos la tupla con los valores de los argumentos de la funcion
estudiante = ("Luis", "Enrique", "Perez", "Corona")

#Pasamos los parametros de la tupla a la funcion con un asterisco al principio para que se detecte como un iterable
imprimir_nombre(*estudiante)

#Dicctionary umpaking, esta forma es bastante similar a la anterior solamente que de esta manera pasamos un diccionario en ves de una tupla 
#Definimos el diccionario
diccionario = {"primer_nombre": "Luis", "segundo_apellido": "Corona", "segundo_nombre" : "Enrique", "primer_apellido": "Perez"}

#Pasamos los valores del diccionario como argumentos de la funcion con dos asteriscos para validar que es un diccionario  
imprimir_nombre(**diccionario)

#Argumentos opcionales, este tipo de argumentos como su nombre lo dice son argumentos que pueden ser o no ser dentro de la funcion
#Ejemplo

#En este caso si no se encuentra un descuento el argumento se estable como opcional en 0
def calcular_precio(nombre_producto, cantidad, precio_u, descuento=0):
    precio_final = cantidad * precio_u * (1-descuento)
    print(f"El precio final para {nombre_producto} es {precio_final}")

calcular_precio("Camisa", 3, 20)


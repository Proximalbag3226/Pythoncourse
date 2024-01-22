#Los returns en el paradigna de la programacion funcional cambian un poco alo que estamos acostumbrados siempre ya que como se explico anteriormente da igual 
#Conocer el funcionamiento internode las funciones solamente nos importa que regresan los mismos valores para las mismas entradas 

#Ejemplo 
def f1(lista):
    return [x * 2 for x in lista]

def f2(palabra):
    return [palabra]

#En este paradigma de la programacion no nos importa que estan realizando internamente f1 y f2 y recordemos que asumimos que para los mismos valores
#De entrada en las funciones van a retornar los mismos valores de salida, para una mejor explicacion y comprension de esto vamos a explicar 
#Un concepto importante para toda la parte de las funciones, el equational reasoning
#Este concepto se refiere a la capacida de tratar de manera mas matematica y de entender el sistema de funcionalidades del codigo a partir de la vision
#Matematica y entender y razonar el codigo como si se tratara de ecuaciones o desigualdades, esto como pude aplicarse dentro de la codificacion
#Por ejemplo al tener la vision de una manera mas matematica y no tan logica como se suele tratar al codigo, en la programacion funcional los programas 
#Son construidos a base de la composicion de funciones y la aplicacion de funciones a argumentos, recordemos que en FP se tiene por sobre todas las cosas
#El uso de las funciones puras La propiedad fundamental de las funciones puras es que producen el mismo resultado para los mismos argumentos, lo que facilita el 
#Razonamiento ecuacional, por ejemplo si una funcion f devuleve un resultado x para un conjunto dado de entradas podriamos remplazar la funcion f 
#Por su resultado x en cualquier parte del programa y este mismo no se veria afectado de ninguna manera 
#El razonamiento ecuacional implica trabajar con ecuaciones y sustituciones para comprender el comportamiento del programa. Esto puede ser útil en la construcción de 
# programas más seguros y comprensibles. Además, facilita la prueba y la verificación del código, ya que puedes analizar y simplificar expresiones de manera algebraica.
#Todo esto se resume a la capacidad de razonar sobre programas tratandolos como ecucaciones.

#Declaremos otra funcion 
def mi_funcion(x,y):
    return f1(x) + f2(y)

#Invocamos para ver que tipos de valores retornan 
print(f1([1,2]))
print(f2('hola'))
print(mi_funcion([3,4], 'ola'))

#Ahora vamos a verificar el equational reasoning ya que podemos ver como reamplazamos el valor retornado de las funciones por su valor directo 
assert mi_funcion([3,4], 'ola') == [6,8, 'ola']
print("Si salio bien")
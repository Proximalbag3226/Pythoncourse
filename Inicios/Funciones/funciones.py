#Funciones en python, las funciones en python son bloques de instrucciones empaquetadas, estas contienen la logica del programa o en este caso de la funcion
#las funciones tambien pueen recibir paramatros que son los "datos" que le pasamos a la funcion y tambien pueden o no retornarnos valores
#Lo anterior mencionado lo podemos definir en coodigo con la palabra "def"

#Definimos la funcion
def saludar():
    print(f"Hola como estas, que tal va tu dia")
    print("Mucho gusto, yo soy Luis")
    print("Zy")
    
#Para ejecutar la funcion despues de definirla tenemos que llamarla 
saludar()

#Podemos utilizar las funciones las veces que queramos dentro del programa 
#Los parametros dentro de las funciones son los que estan contenidos dentro de los parentesis de las funciones 
#En este caso estamos definiendo un saludo con el parametro "nombre"
def saludo_nombre(nombre):
    print(f"Hola {nombre} mucho gusto y que tengas buen dia")
    
#Y al llamar a la funcion especificamos el parametro que le apsaremos a la funcion
saludo_nombre("Enrique")

#Los parametros de las funciones pueden ser de diferentes tipos de datos o listas
#El polimorfismo en Python se refiere a la capacidad de objetos de diferentes tipos (clases) de responder al mismo método o función de manera coherente. 
#Esto significa que puedes utilizar una interfaz común para interactuar con diferentes tipos de objetos, siempre y cuando esos objetos implementen los métodos 
#O funciones requeridos. Existen dos tipos principales de polimorfismo en Python: polimorfismo de método y polimorfismo de función.

#Polimorfismo de método: e este tipo de polimorfismo varias clases tienen metodos con el mismo nombre y estas clases pueden ser tratatas 
#Desde una interfaz en comun 

class Perro:
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau, miau!"

def hacer_sonar(animal):
    return animal.hacer_sonido()

# Crear instancias de diferentes clases
perro = Perro()
gato = Gato()

# Llamar al método común a través de la interfaz común
print(hacer_sonar(perro)) 
print(hacer_sonar(gato))   

#Ambas clases tienen el metodo hacer_sonar podemos tratar a objetos de estas clases de maneras iguales

#Polimorfismo de funcion: En este caso se refiere a la capacidad de una funcion de recibir argumentos de distintos tipos y realizar operaciones basadas en estos
#Esto es en parte posible por que python maneja de manera dinamica los tipos de datos

#En este caso la funcion sumar puede haceptar diferentes tipos de datos ehinterpretarlos para que pueda retornar un resultado
def sumar(a, b):
    return a + b

# Usar la función con diferentes tipos de datos
print(sumar(5, 3))   
print(sumar("Hola", "Mundo"))  
print(sumar([1, 2, 3], [4, 5, 6]))  

#La herencia es otro de los pilares fundamentales de la POO esta hace referencia a la capacidad de que una clase herede los atributos y metodos de otra 
#Promoviendo asi la reutilizacion de codigo y la creacion de jerarquias como son las de padres eh hijos
#En lugar de crear una clase completamente nueva desde cero, puedes aprovechar y extender una clase existente, 
#lo que promueve la reutilización del código y facilita la organización de la lógica del programa.

#Clase padre: clase original de donde se heredan los atributos y metodos, tambien llamada supercalse o clase base
#Ejemplo

#La clase padre animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Y un metodo
    def sonido(self):
        print("*Hace un sonido epicamente*")    

#La clase hija de nombre perro a la cual pasamos como argumento la clase padre
class Perro(Animal):
    def ladrar(self):
        print("*Ladra epicamente*")
        
    #Y sobreescribimos el metodo de la clase padre
    def sonido(self):
        print("El perro ladra")

#Cramos otra clase hija
class Gato(Animal):
    def maullar(self):
        print("*Maulla epicamente*")
    
    #Y usamos el metodo super para llamar el metodo de la clase padre. Este metodo ayuda a acceder y ejecutar los metodos de la clase padre
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

#Sobreescirtura de metodos: Es la capacidad de una clase hija de porporcionar su propia implemetacion de un metodo que ya existe en la clase padre
pero = Perro("Jack")
pero.sonido()
gato = Gato("Habanero", "Naranjo")
gato.sonido()
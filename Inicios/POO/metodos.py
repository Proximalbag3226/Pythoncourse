#Los metodos como ya se explico en la introduccion de la poo son las acciones o comportamientos que puede realizar un objeto de una clase 
#En esta parte vamos a profundizar mas en algunos de los metodos de instancia, de clase y estaticos 

#Los metodos de instancia que son los que se han mostrado mas comun hasta ahora, son los que actuan sobre una instancia especifica de la clase
#Ejemplo 

#Creamos la clase
class Nombre_edad:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Creamos un metodo de instancia
    def saludar(self):
        print(f"Hola yo soy {self.nombre} y tengo {self.edad} años")

#Cremos las instancias de la clase
persona1 = Nombre_edad("Luis", 20)
persona2 = Nombre_edad("Fer", 25)

#Llamamos al metodo 
persona1.saludar()
persona2.saludar()

#Los siguientes son los metodos de clase, estos a diferencia de los metodos de instancia tienen acceso a las propidades de la clase en general y no a 
#Los atributos de las instancias particulares de la clase, ademas se pueden identificar facilmente por que se utiliza el decorador @classmethod para definirlos
#Ejemplo 

#Creamos la clase
class Circulo:
    
    #Aqui definimos un atributo de la clase
    pi = 3.141592
    
    #Y aqui un atributo de instancia
    def __init__(self, radio):
        self.radio = radio
    
    #Definimos un metodo de clase que cambie el valor de pi    
    @classmethod
    def pi_nuevo(cls, nuevo_pi):
        cls.pi = nuevo_pi
    
    #Y otro metodo que nos regresa el radio dado un diametro nuevo 
    @classmethod
    def diametro(cls, diametro):
        radio = diametro / 2
        return cls(radio)

#Imprimimos la instancia de clase
print(Circulo.pi)

#Ahora con el metodo de clase actualizamos e imprimimos el nuevo valor de pi
Circulo.pi_nuevo(3.14)
print(Circulo.pi)

#Y ahora creamos un ciruculo que nos va a regresar el radio dado el diametro nuevo
circulo1 = Circulo.diametro(10)
print(circulo1.radio)

#Y por ultimo los metodos estaticos son algo diferentes a los dos anteriores ya que a pesar de que ambos antes mencionados pueden acceder a las
#Propiedades de la clase o de las instancias de la misma, los metodos estaticos no pueden acceder a ninguna de las dos (ni a los de la clase o de las instancias)
#Estos son mas bien como funciones asignadas a una clase pero que no ocupan sus atributos, se usa el decorador @staticmethod para definirlos (auque es opcional)

#Ejemplo

#Definimos la clase
class Operaciones:
    
    #Creamos el metodo estatico para sumar dos numeros
    @staticmethod
    def sumar(a, b):
        return a + b
    
    #Creamos otro pero para restar
    @staticmethod
    def restar(a, b):
        return a - b

#Ahora asigamos cada uno a un resultado
resultado1 = Operaciones.sumar(5, 7)
resultado2 = Operaciones.restar(10, 4)

#Imprimomos los resultados
print(resultado1)
print(resultado2)
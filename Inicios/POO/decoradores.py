#En python un decorador es una forma de modificar o extender el comportamiento de funciones o metodos, en terminos mas estrictos un decorador es 
#Funcion que toma una funcion y la modifican haciendo la sintaxis mas limpia y legible para ciertas tareas
#Algunos ejemplos de decoradores

#Property, este decorador se utiliza para convertir un metodo en una propiedad
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre

#x.setter, este decorador casi siempre es el que acompaña a un property y sirve para establecer un nuevo valor, y tambien permite realizar 
#Validaciones antes de asignar un valor (x hace referencia al nombre de la propiedad en cuestion)

class Edad:
    def __init__(self, edad):
        self._edad = edad
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad <= 0:
            raise ValueError("Edad no valida")
        else:
            self._edad = nueva_edad   
            
#Otro decorador que tambien puede acompañar al property es el @property.deleater, este decorador se utiliza en las funciones cuando se quiere 
#definir la logica que sera ejecutada cuando sea eliminado un atributo gestionado por property
#Ejemplo 
class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    @property
    def nombre_lista(self):
        return self.apellido + self.nombre
    
    @nombre_lista.setter
    def nombre_lista(self, nombre_completo):
        if self.apellido or self.nombre == None:
            raise ValueError("Datos inexistentes")
        else:
            self.nombre, self.apellido = nombre_completo.split(' ')
    
    @nombre_lista.deleter
    def nombre_lista(self):
        print("Eliminando")
        self.nombre = None
        self.apellido = None

alumno1 = Alumno("Juan", "Hernandez")
print(alumno1.nombre_lista)
alumno1.nombre_lista = 'Pedro Perez'
print(alumno1.nombre_lista)
del alumno1.nombre_lista
print(alumno1.nombre_lista)
#Wraps este se utiliza para preservar la informacion de metedatos de la funcion decorada como lo son, su nombre, su documentacion etc.
#Para utilizar este decorador nesesitamos importarlo desde functools 
#Ejemplo 
from functools import wraps

def decorador(func):
    @wraps(func)
    def decorada(*args, **kwargs):
        "Ejemplo de documentacion de la funcion decorada por wraps"
        print("Hola mundo esta es una funcion con wraps")
        return func(*args, **kwargs)
    return decorada

@decorador
def mi_funcion():
    "Esta es la documentacion de la funcion original" 
    print("Hola mundo esta es la funcion original")

#Accedemos a los metadatos de la funcion decorada y de la funcion original 
print("Funcion decorada", mi_funcion.__name__)
print("Documentacion de la funcion decorada", mi_funcion.__doc__)    

#Estos son solamente algunos de los decoradores ya que los mismos se pueden combinar entre si para las diferentes situaciones y como sean los requerimientos 
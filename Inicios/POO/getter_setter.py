#Los getter y setter son metodos especiales que se utilizan en la programacion orientada a objetos (POO) que sirven para 
#Acceder y modificar las propiedades de una clase de manera controlada. Estos metodos son la base del encapsulamiento

#Getter, este metodo es el que se utiliza para obtener el valor de un atributo privado y da acceso a solo lectura de dicho atributo 
#Los metodos empiezan por conveniencia con get 
#Ejemplo 
class Persona:
    def __init__(self, nombre):
        #Definimos el atributo privado nombre  
        self._nombre = nombre
        
    #Y una funcion que retone el nombre 
    def get_nombre(self):
        return self._nombre
    
#Usamos get para obtener este atributo privado 
persona = Persona("Fer")
print(persona.get_nombre())

#Setter, este metodo a diferencia del getter se utiliza para modificar el valor de un atributo privado, con el set si podemos modificar 
#Ya que nos permite el acceso y la modificacion de los aitrbutos privados de una clase y permitir validaciones antes de la asignacion
#Los metodos empiezan por conveniencia con set
#Ejemplo
class Persona2:
    def __init__(self, nombre):
        #Cremos un atributo privado
        self._nombre = nombre
    
    #Creamos la funcion set para asignar un nuevo nombre
    def set_nombre(self, nuevo_nombre):
        
        #Y una validacion para este mismo
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise TypeError("El nuevo nombre no es valido")
    
    #Y ahora una funcion get que nos retorna el nuevo nombre creado
    def get_nombre(self):
        return self._nombre

#Usamos set para acceder y modificar el nombre ya establecido 
persona2 = Persona2("Luis")
persona2.set_nombre("Enrique")
print(persona2.get_nombre())

#Veremos unos de lo pilares de la poo el encapsulamiento
#El encapsulamiento hace referencia a la capacidad de de poder ocultar las propiedades internas de un objetosy restringir sus propiedades, mientas
#Se expone una interfaz publica con la cual interactuar, las caracteristicas de encapsulamiento son las siguientes:
#Ocultamoiento de destalle internos: Como se mencionaba antes, los detalles internos de un objeto como sus metodos y atributos se ocultan,
#Esto significa que los componentes internos no son accesibles desde afuera del objeto 
#Acceso controlado: El acceso a los metodos y atributos de un objeto se realiza con metodos publicos que proporciona el objeto 
#Proteccion de los datos: Al tener protegidos los atributos privados de un objeto podemos proteger los datos que sean nesesarios,
#Ademas podemos aplicar validaciones y reglas de negocio para garantizar su seguridad
#Modificacion controlada de datos: Los cambios en la implementacion interna de un objeto no deberan afectar al cliente que utiliza la 
#Interfaz publica

#Cabe recordar que python al ser un lenguaje mas flexible que otro como podria ser Java no tiene restricciones estrictas al acceso de datos 
#Esto es mas por convencion de buenas practicas como el uso de guiones bajos y el nombramiento de los metodos set y get, a pesar de no 
#Por eso mismo es nesesario mantener las buenas practias en python en especial en la POO ya que llega a ser muy util a la hora de 
#Desarrollar proyectos 
#Ahora si, Mucho texto ahora ejemplos 

#Creamos una clase
class Pikachu:
    #Y un atributo de clase
    tipo = "Electrico"
    
    #Vamos a declarar varios atributos tanto privados como publicos 
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        #Asi como en un combate podremos ocultar el nivel, el voltaje y el amperaje, esto recordemos que en python no podemos hacerlo de manera 
        #Estricta y por lo tanto en vez de que sea una declaracion comun vamos a incluir dentro de ella un guion bajo en el atributo 
        self.nombre = nombre
        self._nivel = nivel
        self.salud = salud
        self._voltaje_max = voltaje_max
        self._amperaje_max = amperaje_max
        self.color = color
    
    #Al igual que atributos privados tenemos metodos privados, estos se definen por conveniencia con un doble guion bajo al principio
    def __obtener_nombre(self):
        return self.nombre
    
    def acceder_metodo_privado(self):
        self.__obtener_nombre()
        
pokemon = Pikachu("Juan", 50, 500, 70, 80, "Rojo")
print(pokemon._nivel)
pokemon.acceder_metodo_privado()

#Falta comentar 
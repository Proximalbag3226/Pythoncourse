#Uno de lo paradigmas de programacion mas importates si no por decir el mas importante es la prorgamacion orientada a objetos(POO), en este tenemos dos cosas 
#Muy importantes, las clases y los objetos, las clases plantillas o prototipos para crear objetos y los obejetos son
#Lo párticulas o que complementa a la clase, los objetos estan contenidos dentro de la clase, asi mismo los objetos estan compuestos de 
#Metodos y atributos,los metodos son las "acciones y comportamientos" que puede realizar el objeto y los atributos son los "estados" del objeto   
#4 Pilares de la programacion orientada a objetos: Encapsulamiento, herencia, polimorfismo y abstraccion 
#Ejemplificaremos la proramacion orientada a objetos con pokemon

#Las clases se definen con la palabra reservada class y se Declaran con la primer letra en mayusculas
#Tenemos dos tipos de atributos, los de clase y los de instancia, los de clase van a ser compartidos por los objetos que se creen a  partir de esa clase
#Los de instancia van a ser especirficos de cada objeto y estos se declaran con los inicializadores 
class Pikachu:
    #atributo de clase
    tipo = "Electrico"
    
    #atributo de instancia
    #Un inizializador es un metodo que se va a ejecutar automaticamente cuando se cree el objeto
    def __init__(self, nombre, lv, salud):
         self.nombre = nombre
         self.nivel = lv
         self.salud = salud
    
    #Creemos un metodo
    def atacar(self):
        #Se usa self para poder acceder a los atributos de la instancia
        print(f"{self.nombre} ataca y realiza {self.nivel/4} de daño")
        
#Creamos el objeto pikachu
Pikachu1 = Pikachu("Pepe", 750, 500)

#Accedemos a los atribuos de clase
print(Pikachu1.tipo)
#Y a los atributos de instancia
print(Pikachu1.nivel)
print(Pikachu1.salud)
print(Pikachu1.nombre)

#Creamos otro objeto
Pikachu2 = Pikachu("Zeus", 1000, 900)
print(Pikachu2.tipo)
print(Pikachu2.nivel)
print(Pikachu2.salud)
print(Pikachu2.nombre)

#Ambos comparten los atributos de clase pero se diferencian en los atributos de instancia 

#Usamos el metodo atacar
Pikachu1.atacar()
Pikachu2.atacar()
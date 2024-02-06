#Metaclases, estas son clases de las clases, es decir que la creacion de las instancias de la clase esta recibe como parametros otras clases 
#Estas son una herramienta util y avanzada de python que permite, las metaclases en este caso son el mecanismo que proporciona python para controlar 
#la creacion de clases. De echo al momento de crear clases en python estas creando una instancia de una metaclase, la metaclase predeterminada de python es
#TYPE

#Ejemplo de metaclase
class MiMetaclase(type):
    def __new__(cls, nombre, bases, diccionario):
        #Modificar o agregar comportamiento antes de que se cree la clase
        diccionario['nuevo_atributo'] = 42
        return super().__new__(cls, nombre, bases, diccionario)

#Usar la metaclase al definir una clase
class MiClase(metaclass=MiMetaclase):
    def __init__(self, valor):
        self.valor = valor

#Crear una instancia de la clase
objeto = MiClase(10)

#Acceder al nuevo atributo definido por la metaclase
print(objeto.nuevo_atributo)

#En este ejemplo, MiMetaclase hereda de type y redefine el método __new__. Este método se llama antes de que se cree la clase y permite modificar o agregar comportamientos 
#Antes de la creación de la clase real.

#Dato importante, las metaclases son una caracteristica mas avanzada de python y no siempre se suelen implementar en todos los programas que vayas a realizar 
#Normalmente son usadas para algunos framworks o bibliotecas avanzadas de python (Como tu vas a utilizar tensorflow, pandas y numpy te sera util aprender bien esto)

#Mas ejemplos con explicacion mas lenta 
class Mi_clase():
    pass

#Creamos una instancia de la clase
uno = Mi_clase()

#Ahora veremos el tipo de la instancia uno 
print(type(uno))

#Y ahora que pasara cuando vemos el tipo de "Mi_clase"
print(type(Mi_clase))

#Es de tipo type, algo raro para ser una clase, esto era lo que explicamos mas arriba, todas las clases de python son derivadas(objetos) de la metaclase type 
#Ahora vamos a crear una clase pero pasando los parametros a la metaclase type

#El primero parametro que pasamos a type, es el nombre de la clase, en este caso, prueba, el segundo parametro es la base para la herencia que podamos hacer
#Como en este caso no haremos ninguna herencia el parentesis queda vacio, y por ultimo el tercer atributo le damos el atributo, los atributos siempre se van a pasar
#Como parametros en tipo de dato de diccionario
prueba_clase = type('Prueba',(),{'valor': 10})

#Aqui podremos obvservar como se crea la clase ocmo instancia de type y podemos comprobar su tipo y el atributo de valor 
print(prueba_clase)
print(type(prueba_clase))
print(prueba_clase.valor)

#Crearemos otra clase para agregarle un metodo con la misma manera que la anterior 

#Cremos el metodo que vamos a agregar posteriormente 
def mi_metodo(self):
    print("Hola")

#Cremos la clase y una instancia de la misma, y como podemos ver pasamos el metodo dentro del diccionario de atributos de la clase
prueba2 = type('Prueba_metodo', (), {'costo': 5, 'mi_metodo': mi_metodo})
prueba3 = prueba2()
prueba3.mi_metodo()

#Otro ejemplo mas de la creacion de propias metaclases 
class Mimeta(type):
    
    #La setenncia __new__ se ejecuta incluso antes que el __init__ y nos sirve para indicar como es que queremos llevar a cabo la construccion del objeto 
    #Como parametros damos el nombre de la clase, su clase base y sus atributos al final vamos a llamar al consctructor type y retonrnar lo que obtenemos
    def __new__(self,class_name, bases, attrs):
        print(f"Nombre {class_name}")
        print(f"Base {bases}")
        print(f"Atributos {attrs}")
        
        #Creamos un atributo propio
        d={}
        for elemento, valor in attrs.item():
            d[elemento] = valor
        d['Mi atributo'] = '55'
        
        return type(class_name, bases, attrs)

class miClase(metaclass = Mimeta):
    a = 5
    nombre = 'Zy'
    
    def imprime(self):
        print(self.nombre * self.a)

objeto1 = miClase()
objeto1.imprime()    
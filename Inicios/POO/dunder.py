#Los "métodos dunder" en Python son métodos especiales que tienen nombres que comienzan y terminan con doble guion bajo (doble underscore), 
# también conocidos como "dunder" (una contracción de "double underscore"). Estos métodos son utilizados para definir comportamientos específicos de 
# objetos en Python. Algunos de los métodos dunder más comunes incluyen:

#__init__(self, ...): Este es el método de inicialización, llamado cuando se crea una nueva instancia del objeto. Se utiliza para inicializar atributos 
# y realizar otras tareas de configuración.
class MiClase:
    def __init__(self, parametro):
        self.atributo = parametro

#__str__(self): Este método define la representación de cadena de un objeto y se llama cuando se utiliza la función str(obj) o print(obj).
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

#__repr__(self): Este método define la representación del objeto y se llama cuando se utiliza la función repr(obj).
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

#__len__(self): Define la longitud del objeto y se llama cuando se utiliza la función len(obj).
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __len__(self):
        return len(self.elementos)

#Ejemplo: 
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return Numero(self.valor + other.valor)

# Uso de la sobrecarga de operadores
num1 = Numero(5)
num2 = Numero(10)
resultado = num1 + num2
print(resultado.valor) 

#DIFERENCIA ENTRE DUNDER Y SOBRECARGA DE OPERADORES
#Cuando se habla de "métodos dunder" (abreviatura de "double underscore"), se hace referencia a los métodos especiales en Python cuyos nombres están rodeados 
# por dos guiones bajos al principio y al final (por ejemplo, __init__, __str__, __add__, etc.). Estos métodos dunder son utilizados para definir el comportamiento 
# de las clases en situaciones específicas, como la inicialización de objetos, la representación de cadenas y, relevantemente, la sobrecarga de operadores.
#Por lo tanto, la sobrecarga de operadores en Python es un caso específico de uso de métodos dunder. Cuando implementas un método dunder específico, como __add__, 
# estás sobrecargando el operador de suma (+) para instancias de tu clase. Similarmente, otros métodos dunder permiten sobrecargar otros operadores y proporcionar 
# comportamientos personalizados para instancias de clases.





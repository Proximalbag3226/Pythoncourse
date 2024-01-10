#En Python, la sobrecarga de operadores se refiere a la capacidad de definir el comportamiento de los operadores estándar para tipos de datos personalizados. 
#Esto se logra mediante la implementación de métodos especiales en las clases, conocidos como "métodos mágicos" o "métodos dunder"
#Comentario echo al terminar esto, cuidado con las sangrias porque luego dan problemas

#Declaramos una clase llamada frutas, que tendra un objeto con nombre y precio
class Fruta:
    def __init__(self,precio):
        self.precio = precio
    
    #Usamos el operador add para realizar la suma de lso precios de dos objetos
    def __add__(self, other):
        if isinstance(other, Fruta):
            return Fruta(self.precio + other.precio)
        else:
            raise TypeError("No se puede sumar Fruta con otro tipo")

fruta1 = Fruta(15.5)
fruta2 = Fruta(23)
suma = fruta1 + fruta2
print(suma.precio)
        
#A continuacion otros operadores que se pueden utilizar y sus ejemplos 
#Operadores Binarios

class Precios:
    def __init__(self, valor):
        self.valor = valor
    
    #Resta
    def __sub__(self, other):
        if isinstance(other, Precios):
            return Precios(self.valor + other.valor)
        else:
            raise TypeError("No se puede restar con otro tipo")
    
    #Multiplicacion
    def __mul__(self, other):
        if isinstance(other, Precios):
            return Precios(self.valor * other.valor)
        else:
            raise TypeError("No se puede multiplicar con el otro valor")

objeto1 = Precios(15)
objeto2 = Precios(20)
resta = objeto2 - objeto1
multipicacion = objeto1 * objeto2
print(resta.valor)
print(multipicacion.valor)

#Para la division cambiaremos un poco el funcionamiento de la clase para que pueda ser obvservado mejor 
#En este caso utilizaremos fracciones, aunqu en este caso no se le llama division si mas mas bien 
#Floordiv
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __floordiv__(self, otra_fraccion):
        if isinstance(otra_fraccion, Fraccion):
            nuevo_numerador = self.numerador * otra_fraccion.denominador
            nuevo_denominador = self.denominador * otra_fraccion.numerador

            # Simplificar la fracción si es posible
            comun_divisor = gcd(nuevo_numerador, nuevo_denominador)
            return Fraccion(nuevo_numerador // comun_divisor, nuevo_denominador // comun_divisor)
        else:
            raise TypeError("No se puede realizar la división entera de Fraccion por otro tipo")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

resultado = fraccion1 // fraccion2
print(resultado.numerador, "//", resultado.denominador)

#Y tambien tenemos la Truediv
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __truediv__(self, otra_fraccion):
        if isinstance(otra_fraccion, Fraccion):
            nuevo_numerador = self.numerador * otra_fraccion.denominador
            nuevo_denominador = self.denominador * otra_fraccion.numerador

            # Simplificar la fracción si es posible
            comun_divisor = gcd(nuevo_numerador, nuevo_denominador)
            return Fraccion(nuevo_numerador // comun_divisor, nuevo_denominador // comun_divisor)
        else:
            raise TypeError("No se puede dividir Fraccion por otro tipo")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

fraccion1 = Fraccion(1, 2)
fraccion2 = Fraccion(3, 4)

resultado = fraccion1 / fraccion2
print(resultado.numerador, "/", resultado.denominador)

#En ambos casos implementamos tambien un algoritmo de ecuclides para poder encontrar el maximo comun divisor 

#Ademas de estos operadores aritmeticos podemos implementar los mismos pero con operadores logicos como podria ser un or, un and, un not o un xor
#Con su respectivo incio de doble guion bajo, ejemplo 

class Binario:
    def __init__(self, valor):
        self.valor = valor
        
    def __and__(self, other):
        if isinstance(other, Binario):
            resultado = self.valor & other.valor
            return Binario(resultado)
        else:
            raise TypeError("No se puede realiazr la operacion and")

binario1 = Binario(0b101)
binario2 = Binario(0b100)
resultado = binario1 & binario2
print(bin(resultado.valor))

#Esto mismo se aplica para otros operadores logicos 

#Por ejemplo or 
class Mayor_precio:
    def __init__(self, precio):
        self.precio = precio
    
    def __or__(self, other):
        if other.precio > self.precio:
            return Mayor_precio(other.precio)
        else:
            return Mayor_precio(self.precio)
        
objeto3 = Mayor_precio(50)
objeto4 = Mayor_precio(20)
mayor = objeto3 | objeto4
print(mayor.precio)
#Ahora tambien tenemos los operadores unuarios que solamente reciben un parametro, como pueden ser para convertir valores 
class Nombre_producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    #Ejemplo de str
    def __str__(self):
        return f"Producto {self.nombre} con precio de {self.precio}"
    
    #Ejemplo de float 
    def __float__(self):
        return self.precio

manzana = Nombre_producto("Manzana", 50)
pera = Nombre_producto("Pera", 30.5)
print(manzana)
print(pera)

#Ejemplo para actualizar el valor de un producto 

class Precio_actulizado:
    def __init__(self, precio):
        self.precio = precio
    
    def __iadd__(self, other):
        self.precio = self.precio + float(other)
        return self
    
articulo1 = Precio_actulizado(50)
articulo1 += 30
print(articulo1.precio)
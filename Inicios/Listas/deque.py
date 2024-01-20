#El deque es una coleccion que puede actuar como pila 

from collections import deque

#tambien podemos hacer las pilas de la siguiente manera con el import de la parte de arriba 
# Crear un deque vacío
mi_deque = deque()

# Añadir elementos al final del deque
mi_deque.append(1)
mi_deque.append(2)
mi_deque.append(3)

# Añadir elementos al principio del deque, esto tiene la palabra left para poder ser mas intuitivo de saber en que parte se va a introducir el elemento
mi_deque.appendleft(0)

print("------------------------Inicia parentesis de explcacion de extend y append-------------------------")
#Ademas de append podemos utiliazr extend, para esto tendremos que hablar y hacer un parentesis para poder explicar correctamente el funcionamiento de cada uno
#Ya que a pesar de que parece que son parecidos tienen una diferencia significativa entre ellos

#Para que la explcacion sea mejor creamos una clase
class Producto:
    def __init__(self, nombre, valor):
        self._nombre = nombre
        self._valor = valor

    def __repr__(self):
        return "nombre:% s valor:% s"% (self ._nombre, self ._valor)

    def get_nombre (self):
        return self ._nombre

    def get_valor (self):
        return self ._valor

#Crearemos una lista con deiferentes productos
chocolate = Producto("Chocolate", 30)
red_bull = Producto("Red Bull", 84)
hamburgesa = Producto("Hamburgesa", 60)

lista_productos = [chocolate, red_bull, hamburgesa]
print(lista_productos)

#Ahora usaremos append para agregar un elemento a la lista
chilaquiles = Producto("Chilaquiles", 35)
lista_productos.append(chilaquiles)
print(lista_productos)

#Y ahora provaremos con extend 
naranja = Producto("Naranja", 5)
#lista_productos.extend(naranja)
#Esta ultima linea de codigo nos hara tener un error en la ejecucion ya que el objeto que le estamos pasando no es iterable
#Eh aqui la diferencia entre append y extend, append simplemente añade el elemento tal cual como esta y extend itera sobre dicho elemento y segun sea 
#Su orden va agregando elemento por elemento, para poder solucionar este problema podemos hacer lo siguiete
lista_productos.extend([naranja])
print(lista_productos)

#Lo que hicimos fue introducir el elemento dentro de una lista que va a poder iterar extend y por lo tanto lo va agregar
#Ahora tambien va un ejemplo que va ser bastante util para el manejo de pilas y deque, que pasa si queremos agregar varios elementos
manzana = Producto("Manzana", 7)
pera = Producto("Pera", 3)
pizza = Producto("Pizza", 89)
productos_nuevos = [manzana, pera, pizza]
lista_productos.append(productos_nuevos)
print(lista_productos)
#Como podemos obvervar si agrego los elementos pero no por separado si no mas bien que agrego toda la lista de elemetos que contenian


#Ahora intentemos con el metodo extend 
lista_productos.extend(productos_nuevos)
print(lista_productos)
#Ahora si se agregaron por separado y no en toda la lista, con todo lo anterior podemos concluir que:
#Append: Agrega cualquier valor completo, por ejemplo, si enviamos un objeto, agrega el objeto, si enviamos una lista, agrega la lista completa en lugar de sus elementos.

#Extend: agrega elementos de una estructura iterable, por ejemplo, si enviamos un objeto puro, no sabe cómo agregarlo, sin embargo, si enviamos ese mismo objeto dentro 
#De una lista, escaneará la lista y agregará ese objeto y, si hay otros, el resto dentro de la lista.

print("------------Fin del parentesis de explicacion de append y extend-------------------")

#Tambien podemos agregar elementos con extend
mi_deque.extend([1,2,3])

#Y al igual que con append tenemos para agregar del lado izquierdo 
mi_deque.extendleft([5,6,7])

# Ver el contenido del deque
print(mi_deque)

# Eliminar elementos al final y al principio del deque
elemento_final = mi_deque.pop()

#Igualmente la palabra left presente para saber de que lado del deque estamos eliminando el elemento 
elemento_inicio = mi_deque.popleft()

# Ver el contenido del deque después de las eliminaciones
print(mi_deque)

#Podemos rotar los elementos a la n derecha o la -n izquierda
mi_deque.rotate(3)
print(mi_deque)

#Podemos poder en orden inverso los elementos
mi_deque.reverse()
print(mi_deque)
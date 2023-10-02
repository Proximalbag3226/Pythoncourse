#Colas, las colas son estructuras de tipó fifo en otras palabras que el primero en entrar es el primero en salir al contrario que las 
#Pilas que el ultimo en entrar es el primero en salir, al igual que estas en python no esta como tal pero podemos imitarla
from collections import deque

cola = ["Maria", "Alejando", "Jose", "Mario"]

#Agregamos elmentos al final de la cola
cola.append("Karla")
cola.append("Flor")
print(cola)

#Sacando el primero elemento de la cola
n = cola.pop(0)
print(n) 
#o tambien
print(cola.pop(0))

#tambien podemos hacer las colas de la siguiente manera con el import de la parte de arriba 

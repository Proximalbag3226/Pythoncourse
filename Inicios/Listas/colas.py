#Colas, las colas son estructuras de tipó fifo en otras palabras que el primero en entrar es el primero en salir al contrario que las 
#Pilas que el ultimo en entrar es el primero en salir, al igual que estas en python no esta como tal pero podemos imitarla
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

#Aqui faltaba una pequeña actualizacion a las colas ya que estabaun poco imcompleto o carente de la suficiente informacion a partir de aqui son la actualizaciones
#Operaciones basicas en la cola
#Ecolar("enqueue"): Agregar elementos a la col, se añaden al final por la naturaleza de la cola 
#Desencolar (dequeue): Eliminar el elemento que está en la parte inicial de la cola
#Frente (front): Obtener el elemento que está en la parte frontal de la cola sin eliminarlo
#Tamaño (size): Obtener el número de elementos en la cola

#Ahora un ejemplo de estas operaciones aplciadas en una cola 

#Creamos una clase con el nombre de cola
class Cola:
    def __init__(self):
        
        #Inizializamos una cola vacia 
        self.items = []

#Definimos una funcion que realizala funcion de encolar usando el metodo append para agregar elementos al  final de la cola
    def encolar(self, elemento):
        self.items.append(elemento)

#Ahora una funcion para desencolar utilizando un if para comprobar si la cola esta vacia primero y si no es asi entonces con pop podemos eliminar el primer elemento
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

#Una funcion para poder obtener el primer elemeto de la cola, esto igualmente usando un condicional if para comprobar el tamaño de la cola y si contiene por lo menos
#Un elemento entonces podemos retornar el indice 0 para obtener el primer elemento 
    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía")

#Para poder obtener el tamaño de la cola es bastante simple ya que al estar definida como una lista con el metodo len podemos obtener su tamaño
    def tamano(self):
        return len(self.items)

#Y si esta vacia entonces hacemos una asignacion del tamaño de la lista a o
    def esta_vacia(self):
        return len(self.items) == 0

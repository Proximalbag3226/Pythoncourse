#Esto es como las colas solamente que implementando su uso con libreria, su comportamiento se define como LIFO lo que significa que el último 
#Elemento agregado es el primero en ser eliminado
#Ejemplo basico de su uso 

#Importamos lo nesesario 
from queue import Queue

# Crear una cola vacía
mi_cola = Queue()

# Encolar elementos
mi_cola.put(1)
mi_cola.put(2)
mi_cola.put(3)

# Obtener y eliminar el elemento en el frente de la cola
elemento_desencolado = mi_cola.get()
print(elemento_desencolado)

# Obtener y eliminar el siguiente elemento en el frente de la cola
otro_elemento_desencolado = mi_cola.get()
print(otro_elemento_desencolado) 

# Verificar si la cola está vacía
esta_vacia = mi_cola.empty()
print(esta_vacia) 

# Obtener el número de elementos en la cola
tamano_cola = mi_cola.qsize()
print(tamano_cola) 


#Aqui algunos metodos que podemos utilizar 
#Queue(): Crea una nueva instancia de la clase Queue. Puedes ajustar el tamaño máximo de la cola (por defecto es infinito) mediante el argumento opcional maxsize.
#put(elemento): Encola un elemento al final de la cola.
#get(): Obtiene y elimina el elemento en el frente de la cola.
#empty(): Verifica si la cola está vacía.
#qsize(): Devuelve el número de elementos en la cola.

#La clase Queue proporciona una implementación segura para hilos (thread-safe) de una cola, lo que significa que puede ser utilizada de manera segura en entornos 
#Con múltiples hilos de ejecución. Si solo estás trabajando en un entorno de un solo hilo, también puedes utilizar una lista como una estructura de cola simple.
#Ten en cuenta que si necesitas una cola de doble extremo (deque), puedes utilizar la clase deque del módulo collections, que proporciona operaciones más eficientes 
#Al principio de la cola

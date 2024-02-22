#En el caso anterior usamos el import de value para poder compartir los datos entre procesos de la
#Pero este solamente nos permite compartir variables en multiproceso pero y en caso de queramos compartir listas 
#O diccionarios o cualquier tipo de coleccion entonces debemos usar Array 
from multiprocessing import Process, Value, Lock, Array
import time 

#Tenemos la funcion proceso que es la que van a utilizar los procesos que recibe como parametro el arreglo
def proceso(lista, lock):
    
    #En este ciclo for recorremos el arreglo con una espera de 0.01 segundos
    for n in range(100):
        time.sleep(0.01)
        
        #Este es un proceso de ejemplo donde va a sumar 1 a todos los elementos de arreglo
        for n in range(len(lista)):
            
            #Y por supuesto dentro de una seccion critica
            lock.acquire()
            lista[n] = lista[n] + 1
            lock.release()

if __name__ == "__main__":
    
    #Creamos la instancia de Array, especificando de que tipo es, en este caso i = int
    lista = Array('i', [1,2,3])
    
    #Creamos el lock
    lock = Lock()
    print(f"Arreglo al incio {lista[:]}")
    
    #Ahora definimos la instancia de los procesos, donde el parametro es el arreglo que compartimos entre los dos procesos
    p1 = Process(target=proceso, args=(lista,lock))
    p2 = Process(target=proceso, args=(lista,lock))
    
    #Iniciamos los procesos
    p1.start()
    p2.start()
    
    #Terminamos los procesos 
    p1.join()
    p2.join()
    
    print(f"Arreglo al final {lista[:]}")
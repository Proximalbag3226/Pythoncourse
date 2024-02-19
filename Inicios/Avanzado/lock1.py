#Ahora veremos como crear una seccion critica y veremos el lock, lock nos sirve para poder crear secciones criticas que nos sirven para delimitar el uso de los 
#Multihilos ya que "cierra" la ejecucion de una porsion de codigo para que solamente sea ejecutada por un solo hilo
#Importamos 
from threading import Thread, Lock
import time

#Vamos a reutilizar el codigo de compartir_datos 
valor = 0 

def procesa(lock):
    global valor
    lock.acquire()
    valor_local = valor
    time.sleep(0.1)
    valor_local = valor_local +1
    lock.release()
    
if __name__ == "__main__":
    print(f"Valor en el incio {valor}")
    
    lock = Lock()
    
    hilo1 = Thread(target=procesa, args=(lock,))
    hilo2 = Thread(target=procesa, args=(lock,))
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
    
    print(f"El valor al final {valor}")
    
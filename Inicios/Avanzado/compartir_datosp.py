#Ahora vamos a ver como compartir datos entre procesos, ya que recordemos que estos no comparten la memoria como si lo hacen los hilos, entonces tenemos que 
#Recurrir a una libreria para poder hacer una memoria compartida para los procesos en este caso Value
from multiprocessing import Process, Value, Lock
import time 

def process(pNumero, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        pNumero.value += 1
        lock.release()        
        
if __name__ == "__main__":
    
    numero = Value('i', 0)
    lock = Lock()
    
    print(f"Numero al incio {numero.value}")
    
    p1 = Process(target=process, args=(numero,lock))
    p2 = Process(target=process, args=(numero,lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Numero al final {numero.value}")
    
#Falta comentar 
#Ahora veremos como compartir los datos entre los hilos ya que recordemos estos comparten la misma memoria y esto ayuda bastante a que sea mas sencilo hacerlo 
from threading import Thread
import time

#Aqui vamos a usar una variable global para simular el dato que vamos a compartir entre los hilos 
valor = 0

#Definimos el metodo qu usaran los hilos 
def procesa():
    
    #Para poder utilizar la variable en un ambito global
    global valor
    
    #Creamos una copia local de la variable local 
    valor_local = valor
    
    print(f"En el hilo el valor es de {valor_local}")
    
    #Y ahora cambiamos su valor 
    valor_local += 1
    
    #Simulacion de que algo mas pasa 
    time.sleep(0.1)
    
    #Depues de la simulacion actualizamos el valor global 
    valor = valor_local

#Ahora pasamos a la creacion de los hilos 
if __name__ == '__main__':
    print(f"El valor de inicio es {valor}")
    
    hilo1 = Thread(target=procesa)
    hilo2 = Thread(target=procesa)
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
    
    print(f"El valor al final {valor}")

#Si obtenemos mas de uno es porque surge una condicion race que nos indica que dos o mas hilos estan tratando de modificar el mismo valor al mismo tiempo
#Por eso mismo utilizamos el sleep para que asi pase al otro hilo sin que aun haya modificado su valor entonces tambien se inicia en 0 


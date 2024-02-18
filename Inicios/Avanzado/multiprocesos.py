#Lo primero a explicar es el GIL por sus siglas Global Interpreter Lock, este es un tipo de lock especial que permite que un solo hilo se ejecute en python
#Esta limitante es nesesaria porque la administracion de memoria en python no es thrated-safe lo cual quiere decir que no es segura cuando el proceso se ejecuta en 
#Multiples hilos, claro que hay implementaciones de python y wrppers que nos sirven para quitar estas limitaciones.
#Ahora, ¿Que es un proceso? Bueno un proceso no es mas que una instancia de un programa y cada uno de ellos es independiente de otro y por lo mismo la memoria no se comparte entre procesos
#Y por lo tanto cada proceso queda en una porcion de memoria diferente y en el caso del procesador, quedar en un nucleo diferente
#Los procesos son lentos en su incio a diferencia del multihilo que inicia automaticamente pero tambien tenemos ventajas como puede ser que son utiles a la hora de 
#Evitar las limitantes del GIL ya que para los multiprocesos se crea un GIL para cada uno de los procesos, pero a cambio de esto la comunicacion entre procesos es mas 
#Complicada que la comunicacion entre los hilos y que ademas los procesos se pueden interrumpir por algun tipo de error o algo asi 

#Ahora si pasemos a la aprte practica de la creacion de multiprocesos con el modulo que ocuparemos 
#Importamos las biblotecas que ocupamos 
from multiprocessing import process
import os
import winsound

#Esta es la funcione que se ejecutara en cada proceso
def function(numero):
    print(os.getpid())
    for i in range (10):
        valor = i*i+i 
        print(f"{valor}---> {numero}")
        winsound.Beep(2500, 100)

#Para la ejecucion en caso de que estes utilizando algun otro programa debes ejecutar los codigos de multiproceso en consola o modificar la configuracion del programa que estes usando 
#Y colocare un main para simplificar 
if __name__ == '__name__':
    
    #Aqui vamos a guardar los procesos 
    procesos = []
    
    #Obtenemos la cantidad de procesos que tenemos 
    cores = os.cpu_count()
    print(f"Tienes {cores} nucleos")
    
    #Ahora vamos a instanciar los procesos, aqui en este caso yo instancio un proceso por nucleo pero si quieres puedes cambiar esto
    for i in range (cores):
        
        #Cremos la instancia y asignamos la funcion nesesaria a ejecutar con sus parametros nesesarios
        proceso = process(target = function, args = (i,))
        
        #Y lo adicionamos a la lista de procesos 
        procesos.append(proceso)
    
    print("Y AHORA EJECUTAMOS")
    
    for proceso in procesos:
        proceso.start()
        
    print("---Espera")
    for proceso in procesos:
        proceso.join()
        
    print("Regresando a la ejecucion incial")
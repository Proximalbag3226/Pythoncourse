#Thread tambien conocidos como hilos son una forma de realizar diferentes tareas dentro de un mismo proceso, estos son mas rapidos que los procesos
#Y es mas sencillo compartir informacion entre ellos ya que coparten la misma memoria otra cosa de diferencia a los procesos es que estos no pueden ser interrumpidos
#Esto ultimo es muy importante ya que debemos ser muy minucios con el manejo de errores para evitar la corrupción de datos 

#Importanmos las bibliotecas 
from threading import Thread
import os 
import winsound
import time 

def function(numero):
    print(os.getpid())
    for i in range (10):
        valor = i*i+i 
        print(f"{valor}---> {numero}")
        winsound.Beep(2500, 100)

#Para la ejecucion en caso de que estes utilizando algun otro programa debes ejecutar los codigos de multihilo en consola o modificar la configuracion del programa que estes usando 
#Y colocare un main para simplificar 
if __name__ == '__name__':
    
    #Aqui vamos a guardar los hilos
    hilos = []
    
    #Obtenemos la cantidad de nucleos que tenemos 
    cores = os.cpu_count()
    print(f"Tienes {cores} nucleos")
    
    #Ahora vamos a instanciar los hilos, aqui en este caso yo instancio un proceso por nucleo pero si quieres puedes cambiar esto
    for i in range (cores):
        
        #Cremos la instancia y asignamos la funcion nesesaria a ejecutar con sus parametros nesesarios
        hilo = Thread(target = function, args = (i,))
        
        #Y lo adicionamos a la lista de hilos
        hilos.append(hilo)
    
    print("Y AHORA EJECUTAMOS")
    
    for hilo in hilos:
        hilo.start()
        
    print("---Espera")
    for hilo in hilos:
        hilo.join()
        
    print("Regresando a la ejecucion incial")
    
    time.sleep(10)
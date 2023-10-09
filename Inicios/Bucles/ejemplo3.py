#En este ejemplo utilizaremos el break para poder ejemplificar como es su funcionamiento dentro de los ciclos

#importamos la librebria de random para uutilizar su metodo de randint mas adelante
import random   

#Definimos las variables que vamos a utilizar para los caracoles y para la meta
meta = 20
caracol1 = 0 
caracol2 = 0

#Iniciamos el ciclo while donde se realizara la carrera y el avance de los caracoles
while True:
    
#Utilizamos el random para generar aleatoriamente la cantidad de espacios que se van a mover, esto en un rango de 1 a 4
    avance_caracol_1 = random.randint(1, 4)
    avance_caracol_2 = random.randint(1, 4) 

#Cambiamos el valor de la varibale por el nuevo valor del movimiento 
    caracol1 += avance_caracol_1
    caracol2 += avance_caracol_2
    
#Imprimimos como va la carrera en la consola 
    print(f"El caracol 1 avanza{avance_caracol_1} y lleva una distancia de {caracol1}")  
    print(f"El caracol 2 avanza{avance_caracol_2} y lleva una distancia de {caracol2}")
    print("----------------------------------------------------------------")
    
#Al haber eclarado el ciclo while con un True tenemos que incluir una instruccion donde se termine el bucle, en este caso el break    
    if caracol1 >= meta or caracol2 >= meta:
        break

#Imprimimos el resultado de la carrera
if caracol1 > caracol2:
    print("El caracol 1 es el ganador")
elif caracol2 > caracol1:
    print("El caracol 2 es el gandor")
else:
    print("Es un empate")
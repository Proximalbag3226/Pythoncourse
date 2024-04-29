#Otro algoritmo para ordenar listas es el quicksort, este algoritmo se basa en dividir la lista en sublistas para ordenar cada una a partir de recursividad 
#Tomamos un indice n de manera aleatoria en la lista y a partir de ahi la dividimos en dos sublistas una con los elementos de igual o menor valor al que tenemos en el indice n 
#Y otra con los elementos de mayor valor y a partir de aqui usamos la recursividad en la funcion para ordenar cada sublista y una vez que esten todas ordenadas 
#Se unen en una sola de nuevo, este algoritmo tiene una complejidad algoritmica big-o de O(nlogn), o en el peor de los casos O(n^2), por lo cual es uno de los mas eficientes y rapidos para grandes volumenes de 
#Elementos aunque no el mas rapido 


#Importamos la biblioteca
from random import randrange
import time 

#Cremos una funcion que ejecute la tarea 
def quick_sort(coleccion: list) -> list:
    
    #Verificamos que tenga una longitud mayor a 2 elementos
    if len(coleccion) < 2:
        return coleccion
    
    #Tomamos un inidice aleatorio dentro de la lista
    pivot_index = randrange(len(coleccion))
    
    #Toma este elemento y lo guarda en una variable aparte de la lista 
    pivot = coleccion.pop(pivot_index)
    
    #Toma los elementos menores o de igual valor al elemento que guardamos antes y los almacena en una lista diferente
    lesser = [elemento for elemento in coleccion if elemento <= pivot]
    
    #Ahora lo mismo pero con los que son mayores
    greater = [elemento for elemento in coleccion if elemento > pivot]
    
    #Usamos la recursividad para llamar la funcion dentro de la misma y desempaquetar las listas para asi volver a repetir el proceso 
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]

#Ejecutamos el codigo 
if __name__ == "__main__":
    user_input = input("Ingresa los numeros separados por una coma pr favor:\n").strip()
    unsorted = [int(elemento) for elemento in user_input.split(",")]
    
    inicio = time.time()
    sorted_list = quick_sort(unsorted)
    fin = time.time()
    print(f"Lista ordenada: {sorted_list}, con tiempo de ejecucion de {fin-inicio} segundos")
#Este algoritmo es como el "hermano" chiquito del quicksort ya que se basa en un principio parecido de funcionamiento que es la division de la lista en sublistas
#Pero a difenrencia del quicksort que las sublistas son de valores menores o iguales que el pivote, en el merge sort se dividen hasta que la longitud de la lista sea 1
#Teniendo asi n cantidad de sublistas dependiendo de la n cantidad de elementos de la lista original y al final usando recursividad se unen las unas a las otras 
#Otro punto de diferencia es la complejidad algoritmica ya que en todos los casos va a ser de O(n log n), entonces en general sus diferencias son:
#Quicksort prioriza la eficiencia en tiempo en la mayoria de casos y mas eficiente en memoria, y mergesort es mas predecible y estable para aplicaciones donde 
#El tiempo de ejecucion previsible es la prioridad 

#Ejemplo del uso de mergesort 
import time

#Cremos una lista 
lista10 = [5,1,90,34,22,2]

#Cremos una funcion que se encarge del ordenamiento de las listas 
def merge(lista1, lista2):
    
    #Una lista vacia nueva
    lista3 = []
    
    #En un ciclo siempre que el valor de las sublistas sea mayor que 0
    while(len(lista1) > 0 and len(lista2) > 0):
        
        #Si el elemento de la sublista 1 es menor que el de la lista2 agragamos ese elemento a la lista nueva 
        if lista1[0] < lista2[0]:
            lista3.append(lista1[0])
            lista1 = lista1[1:]
        
        #En caso contrario agregamos el otro 
        else:
            lista3.append(lista2[0])
            lista2 = lista2[1:]
    
    #Comprobamos que la lista ya este vacia
    if len(lista1) > 0:
        lista3 = lista3 + lista1
    
    if len(lista2) > 0:
        lista3 = lista3 + lista2
    
    #Retornamos la nueva lista 
    return lista3
    
#Ahora una funcion para unir
def merge_sort(lista):
    
    #Validacion 
    if len(lista) == 1:
        return lista
    
    #Encontrar el punto medio de la lista
    l1 = lista[:len(lista)//2]
    l2 = lista[len(lista)//2:]
    
    #Recursividad para las sublistas
    l1 = merge_sort(l1)
    l2 =  merge_sort(l2)
    
    #Llamamos a merge 
    return merge(l1, l2)



print(lista10)
inicio = time.time()
ordenado = merge_sort(lista10)
fin = time.time()
print(f"La lista ordenada es: {ordenado}, con tiempo de ejecución: {fin-inicio} en segundos ")
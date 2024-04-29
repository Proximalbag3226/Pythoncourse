#El algoritmo bubble sort entra dentro de la categoriad de algoritmos de ordenamiento que sirven como su nombre meciona para ordenar una lista de datos, en este caso numeros
#De menor a mayor hasta que se terminen los terminos de la lista, este algoritmo tiene el punto fuerte que es bastante util en listas pequeñas por su simplicidad y su 
#Capacidad de identificar errores rapidamente a menor cantidad de elementos de la lista, no se recomienda su uso en listamuy grandes de elementos ya que su crecimiento 
#De complejidad algoritmica de big-o esta determinada por O(n^2)

#Pasemos al ejemplo simple de este algoritmo para el ordenamiento de una lista 
#Usaremos time para comprobar el tiempo de ejecucion del algoritmo
import time

#Definimos la lista de datos de manera desordenada 
lista1 = [1,9,14,6,7,2,20]

#Cremos una funcion que realize la tarea de ordenamiento
def bubble_sort(lista):
    
    #Tomamos como valor de longitud la lista menos 1 
    l = len(lista)-1
    
    #En un ciclo for desde 2 hasta el valor penultimo de la lista
    for i in range(1, l):
        
        #Y en el for anidado vamos recorriendo valores de la lista hasta la longitud -1
        for j in range(0, l-1):
            
            #Ponemos la condicion que si el elemento iterado es mayor que el siguiente estos cambiaran lugar
            if lista[j] > lista[j+1]:
                i = lista[j]
                lista[j] = lista[j+1]
                lista[j + 1] = i
                
    #Rtornamos la lista ya ordenada 
    return lista

#Medimos el tiempo de ejecucion
inicio = time.time()
lista_ordenada = bubble_sort(lista1)
fin = time.time()

#Imoprimimos los resultados
print(f"La lista ordenada es: {lista_ordenada}")
print(f"Y tuvo un tiempo de ejecucucion de {fin-inicio} segundos")
                                                                                                                
#Para listas pequeñas el tiempo es imperceptible pero esto cambia segun la longitud de la lista en cuestion
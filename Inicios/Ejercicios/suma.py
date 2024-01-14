#Obtener la maxima suma de dos elementos adyacentes en una lista

#Definimos la funcion que va a relizar esto 
def max_sum(lista):
    
    #Comprobamos que tenga mas de 2 elementos la lista que se le paso a la funcion 
    if len(lista) < 2:
        raise TypeError("La lista no contiene elementos sufientes")
    
    #Inicialisamos con el valor infinito negativo 
    maxima_suma = float('-inf')
    
    #Y con un bucle for vamos recorriendo la lista hasta un valor antes del final de la lista
    for i in range(len(lista) - 1):
        
        #La suma actual sera el valor actual mas el valor siguiente
        suma_actual = lista[i] + lista[i + 1]
        
        #Y encontramos la mayor de esas sumas
        maxima_suma = max(maxima_suma, suma_actual)
    return maxima_suma


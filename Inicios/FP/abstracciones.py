#En la programcion funcional tenemos abstracciones al igual que en la orientada a objetos tenemos las abstracciones que es la capacidad de manejar 
#conceptos complejos y simplificarlos para su optimization, pero a diferencia que en POO en FP al no tener clases la abstraccion se llevara a cabo a travez 
#De funciones, esto es util para la reutilizacion de codigo y la facil depuracion del mismo. 

#Ejemplo

#Crea una funcion la cual recibira una lista de numeros y el resultado debera ser la lista con cada elemento aumentado en 1 
#Como en FP no podemos utilizar bucles usamos la recursividad de la funcion
def incrementar_1(list_numeros):
    #Si ña lista esta vacia retornamos la vacia 
    if list_numeros == []:
        return []
    
    #En caso contrario retornamos una lista que contiene numeros en el indice 0 + 1 y concatenamos la lista para volerla a pasar pero ahora con el indice 1 y asi en adelante
    else:
        return [list_numeros[0]+1] + incrementar_1(list_numeros[1:])

print(incrementar_1([1,2,3]))

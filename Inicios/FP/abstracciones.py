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

#Hagamos el mismo ejemplo pero con 2 
def incrementar_2(list_num):
    if list_num == []:
        return []
    
    else:
        return[list_num[0]+2]+ incrementar_2(list_num[1:])

print(incrementar_2([2,3,4]))

#Pero si nos damos cuenta esta forma es poco util cuando queremos incrementar n cantidad de numeros de manera mas simple ya que si no tendiramos que crear n funciones
#Para incrementar n cantidad de numeros a la lista, entonces vamos a crear una funcion que se encarge de esto usando la abstraccion de la FP

#La funcion incrementar_n recibe como parametros una funcion y la lista de numeros, para esto recordemos que en FP las funciones como argumentos pueden recibir otras funciones
#Como si fueron de orden superior
def incrementar_n(f, num_list):
    if num_list == []:
        return []
    
    #Dentro del else retornamos la lista con el incremento que de la funcion que se va a pasar como argumento
    else:
        return[num_list[0]] + incrementar_n(f, num_list[1:])

#En esete caso vamos a utilizar un funcion lamnda para poder simplificar el proceso y hacerlo mas eficiente, esta puede sumar cualquier numero en este caso 3
print(incrementar_n(lambda n: n+3, [1,2,3]))

#Ahora otros dos ejemplos mas de la recursion de funciones para mas adelante usar las abstracciones
def conteo(lista):
    if lista == []:
        return 0 
    else:
        return 1 + conteo(lista[1:])

print(conteo([1,2,3,4]))

def suma_lista(lista):
    if lista == []:
        return 0 
    else:
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([5,6,7]))

#La siguiente es una abstraccion sensilla y de ejemplo que nos va a servir cuando deseemos adicionar numeros basados en una lista
def conteo_suma(f,lista):
    if lista == []:
        return 0 
    else:
        return f(lista[0]) + conteo_suma(f,lista[1:])

#Ahora utilizaremos sus dos ejemplos de uso
print(conteo_suma(lambda n: 1, [1,2,3,4]))
print(conteo_suma(lambda n: n, [1,2,3,4]))
#Como podemos obvservar estas funciones llevan a cabo las tareas de las declaradas mas arriba, suma_lista y conteo, pero ahora en una sola funcion y con lambda 
#Esto es la prueba mas clara de abstraccion ya que estamos simplificando su concepto y optimizando estas mismas funciones en una sola y de manera mas eficiente 
#Y si cambiamos los valores de las listas estan tendran el mismo resultado de las anteriores, ya que si obvservamos bien cada una de las lambda retorna 
#Uno de los valores que las funciones conteo y suma_lista ya retornaban en si mismas y como cereza del pastel tambien implementamos la recursion dentro del codigo 
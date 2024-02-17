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

#Bien ahora vamos a crear abstracciones mas complicadas     
def mayor(numeros, mayor_actual = 0):
    if numeros == []:
        return mayor_actual
    else:
        if numeros[0] > mayor_actual:
            mayorN = numeros[0]
        else:
            mayorN = mayor_actual
    return mayor(numeros[1:], mayorN)

print(mayor([1,2,3,4,5,5,15]))

#En esta funcion lo que hacemos es generalizar las acciones que realizamos en las abstracciones pasadas
def reducida(f, lista, acc):
    
    #Si obvservamos bien cada funcion pasada contiene una primera condicion que nos retorna algo en caso de que la lista este vacia
    if lista == []:
        
        #En este vamos a almacenar lo que retorna la condicion en la variable acc
        return acc
    else:
        
        #En caso contrario podremos ejecutar la funcion que se proporcione como argumento y que aplicaremos a la lista en su indice 0 proporcionando tambien el acc
        #Ya que las funciones que hicimos anteriormente cumplen con dicha condicion de argumentos que podemos pasar como son la lista podemos simplñificarlas aqui
        accN = f(lista[0], acc)
        
        #Y por ultimo realizamos la recursion nesesaria para el correcto funcionamiento 
        return reducida(f, lista[1:], accN)

#Ahora teniendo la "plantilla" del codigo para realizar las accines pasadas vamos a replicar las funciones anteriores pero ahora usando esta nueva abstraccion 
#Y obviamente con funciones lambda para optimizar
def mayor(lista):
    return reducida(lambda num, acc: num if num>acc else acc, lista, 0) 

def conteo(lista):
    return reducida(lambda _, acc : acc +1, lista, 0)

def sumatoria(lista):
    return reducida(lambda num, acc: num+acc, lista, 0)  

print("Mayor", mayor([12,3,7,8,14]))
print("Conteo", conteo([1,2,3,45,12]))
print("Sumatoria", sumatoria([1,2,3,4]))

#Usaremos la funcion de reduccion para ver si podemos simplificar el incremento de 1 
def mapeo(f,lista):
    #Aqui realizamos la concatenacion de lo que nos retornaba la lista
    return reducida(lambda el, acc: acc + [f(el)], lista, [])

def incrementa_1(lista):
    return mapeo(lambda n: n+1, lista)

print(incrementa_1([1,2,3,4,5]))

#Ahora vamos a utilizar herramientas de codigo mas modernas, que en si no se deberian utilizar en FP ya que es preferible la recursividad por sobre la iteracion de elementos
#Pero para que sea mejor visualizado usaremos ciclos for para los siguientes ejemplos 

def reducida(f, lista, acc):
    for el in lista:
        acc = f(el, acc)
    return acc

def mayor(lista):
    return reducida(lambda x, acc: x if x>acc else acc, lista, 0)
    
def conteo(lista):
    return reducida(lambda _, acc: acc+1, lista, 0)

def sumatoria(lista):
    return reducida(lambda x, acc: x+acc, lista, 0)

def mapeo(f,lista):
    return reducida(lambda x, acc: acc+[f(x)], lista, [])

def incrementar1(lista):
    return mapeo(lambda x: x+1, lista)

print("Mayor", mayor([7,34,5,234,5]))
print("Conteo", conteo([8,5,4,3,2,1]))
print("Sumatoria", sumatoria([1,67,1,4,5,1]))
print("Incrementar1", incrementar1([1,2,5,67,2]))

#Ahora algunos ejemplos donde podemos utilizar la reutilizacion de codigo en el paradigma de FP donde tambien podemos implementar las abstracciones 
#Podemos parametrizar algun tipo de codigo pero con diferntes casos por ejemplo: 
def noc(x):
    return x+5

#Generalizamos sobre un computo en especial y si nos damos cuenta las funciones son muy similares entre si y es mucho trabajo y repeticion estar 
#Repitiendo los prints y las funciones asi:

def f1(x):
    print(f"En f1 el valor inicial es {x}")
    r = f2(x) + f3(x)
    print(f"El valor final es de {r}")
    return r

def f2(x):
    print(f"En f2 el valor inicial es {x}")
    r = x*2
    print(f"El valor final es de {r}")
    return r
def f3(x):
    print(f"En f3 el valor inicial es {x}")
    r = x-5
    print(f"El valor final es de {r}")
    return r

print(f1(10))

#Ahora vamos a generalizar el codigo 
def fn(nombre, f, x):
    print(f"En {nombre} el valor inicial es de {x}")
    r = f(x)
    print(f"El valor final es de {r}")
    return r

def f11(x):
    return fn("f11", lambda x: f2(x) + f3(x), x)

def f21(x):
    return fn("f21", lambda x: x*2, x)

def f31(x):
    return fn("f31", lambda x: x-5, x)

f11(10)

#Y si aun queremos reducir aun mas el codigo podemos utilizar decoradores para mejorar el codigo y su legibilidad

#Aqui creamos y definimos nuestro decorador donde recibimos la funciona a decorar y retorna los "atributos" de la fn
def f_decorador(f):
    
    #El nombre de la funcion lo obtenemos de .__name__ pasamos f que es la funcion y el valor de x 
    return lambda x: fn(f.__name__,f,x)

@f_decorador
def f1_1(x):
    return f2_2(x) + f3_3(x)

@f_decorador
def f2_2(x):
    return x *2

@f_decorador
def f3_3(x):
    return x - 5
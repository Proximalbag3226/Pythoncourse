#Timeit es un modulo de python que fue diseñado para poder medir el tiempo de ejecucion que tienen pequeñas porciones de codigo, esto es muy util a la hora de 
#Evaluar rendimiento de alguna funcion o dicha parte del codigo
#Ejemplo basico de el uso de este modulo para la medicion del tiempo de ejecucion 

#Importarmos el modulo
import timeit

# Definir la expresión o la función a medir
codigo = """
for i in range(1000):
    _ = i * i
"""

# Medir el tiempo de ejecución utilizando timeit
tiempo = timeit.timeit(codigo, number=10000)

#Imprimimos el resultado de la medicion 
print(f"Tiempo de ejecución: {tiempo} segundos")

#Podemos tambien evaluar el tiempo de ejecución de las funciones 

# Definir la función a medir
def mi_funcion():
    for i in range(1000):
        _ = i * i

# Medir el tiempo de ejecución de la función utilizando timeit
tiempo = timeit.timeit(mi_funcion, number=10000)

print(f"Tiempo de ejecución: {tiempo} segundos")
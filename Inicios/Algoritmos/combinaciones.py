#Tenemos un ejemplo de como generar todas las combinaciones de longitud m en los valores de 1 a n
from itertools import combinations
from typing import List

#La fucnion genera las diferentes combinaciones en un rango de 1 a n de longitud m donde:
#m = Longitud de la lista que es reotrnada por la funcion 
#n = Valor del numero maximo que puede tomar la lista ej. n = 4 entonces -> [1,2,3,4]
def combination_lists(n: int, m: int) -> List[List[int]]:
    
    #Comprobamos una serie de argumentos que deben ser cumplidos para que seejecute correctamente
    #En este caso comprobamos que los valores n y m sean te tipo entero (int), tambien se comprueba que ambos sean menores a 0 o que m sea mayor a n
    #En caso de que alguna de estas condiciones no se cunmpla se despliega la alerta en la consola de errores
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0 or m > n:
        raise ValueError("Los argumentos n y m deben ser enteros no negativos, y m no puede ser mayor que n.")

    return [list(combination) for combination in combinations(range(1, n + 1), m)]

# mprimimos los resultados en caso de que las coniciones de los datos sean correctas
try:
    n_value = int(input("Ingrese el valor de n: "))
    m_value = int(input("Ingrese el valor de m: "))
    result = combination_lists(n_value, m_value)
    print(f"Todas las combinaciones posibles de longitud {m_value} a partir de la secuencia de 1 a {n_value}:")
    print(result)
    
#Si tenemos algun error en la ejecucion se despliega 
except ValueError as ve:
    print(f"Error: {ve}")

    
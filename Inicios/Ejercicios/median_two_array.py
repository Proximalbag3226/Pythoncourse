#En este ejercicio tenemos como objetivo calcular la mediana de dos listas ORDENADAS

#Definimos la funcion que se encragara de este trabajo, esta recibe dos listas 
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    
    #Comprueba que ambas listas esten vacias y si es asi devuleve el error
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    #Combinamos las dos listas en una sola con el metodo sorted
    merged = sorted(nums1 + nums2)
    
    #Calculamos la longitud total de la nueva lista creada
    total = len(merged)

    #Comprobamos si la cantidad de elementos en la nueva lista es par o impar, en caso de ser impar devolvemos el valor central
    if total % 2 == 1: 
        return float(merged[total // 2]) 

    #En caso de ser par encontramos los dos valores centrales y los promediamos devolviendo su valor en flotante 
    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]
    return (float(middle1) + float(middle2)) / 2.0

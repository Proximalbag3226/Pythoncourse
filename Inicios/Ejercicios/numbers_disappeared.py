#Se da un array de n numeros enteros donde nums[i] es el rango y tenemos que retornar todos los numero enteros faltantes en al array 
def numbers_disappeared(list):
    for n in list:
        i = abs(n) -1
        list[i] = -1 * abs(list[i])
    
    res = []
    for i, n in enumerate(list):
        if n > 0:
            res.append(i + 1)
    return res        
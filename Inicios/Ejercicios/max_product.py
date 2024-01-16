def encontrar_multiplicacion_mas_grande(lista):
    if len(lista) < 2:
        return "La lista debe contener al menos dos números."

    multiplicacion_mas_grande = lista[0] * lista[1]

    for i in range(1, len(lista) - 1):
        multiplicacion_actual = lista[i] * lista[i + 1]
        multiplicacion_mas_grande = max(multiplicacion_mas_grande, multiplicacion_actual)

    return multiplicacion_mas_grande

# Ejemplo de uso
numeros = [3, 7, 2, 5, 10]
resultado = encontrar_multiplicacion_mas_grande(numeros)
print("La multiplicación más grande de dos números adyacentes es:", resultado)

from random import randrange

def quick_sort(coleccion: list) -> list:
    if len(coleccion) < 2:
        return coleccion
    pivot_index = randrange(len(coleccion))
    pivot = coleccion.pop(pivot_index)
    lesser = [elemento for elemento in coleccion if elemento <= pivot]
    greater = [elemento for elemento in coleccion if elemento > pivot]
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    user_input = input("Ingresa los numeros separados por una coma pr favor:\n").strip()
    unsorted = [int(elemento) for elemento in user_input.split(",")]
    
#Falta comentar este algoritmo pero a resumen es uno de los usados para el ordenamiento de listas 

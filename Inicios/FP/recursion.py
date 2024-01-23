#Como recordemos en la programacion funcional no tenemos los ciclos iterativos como pueden ser el for o wl while si no mas bien en cambio de eso 
#En FP se prefiere la recursividad para solucionar los problemas que requieren una analisis de bucle al problema, el termino recursividad hace referencia 
#Al echo y caracteristica de un programa o funcion de que se invoque a si mismo una n cantidad de veces en el tiempo, esto lo hara de manera indeterminada
#Hasta que el problema dado no sea resuelto, en el paradigma de la FP la recursividad se utiliza para dividir el problema dado en mas subproblemas para que 
#Cada uno de ellos pueda ser solucionado por separado

#Ahora un ejemplo de funciones con recursividad 
def suma(lista):
    
    #Verificamos que la lista tenga elementos
    if lista == []:
        return 0
    
    #Invocamos la funcion dentro de ella misma usando recursividad 
    else:
        return lista[0]+suma(lista[1:])
print(suma([1,2,3,4,5]))

#Otro ejemplo pero ahora con recursividad de clases 
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

class Grupo():
    def __init__(self, miembros, subgrupos):
        self.miembros = miembros
        self.subgrupos = subgrupos
        
def obtener_todos(grupo):
    subMiembros = []
    for subgrupo in grupo.subgrupos:
        subMiembros.extend(obtener_todos(subgrupo))
    return grupo.miembros + subMiembros
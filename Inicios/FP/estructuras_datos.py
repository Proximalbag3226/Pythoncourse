#Ahora vamos a ver como sera el uso de las estructuras de datos enfocado al paradigma de FP, recordemos que como se habia mencionado el principio en FP se prefiere por sobre todo
#La inmutabilidad en las estructuras de datos por lo tanto las tuplas son fundamentales para este paradigma ya que la mutabilidad de las estructuas de datos puede 
#Generar problemas dentro de la aplicacion, ya que en FP lo que se nesesita son datos de alta confianza y fiabilidad para su posterior uso 

#Ejemplo

#Aqui vamos a mutar la lista 
def adiciona(lista):
    lista.append("Manzana")
    return lista

milista = ["Pera", "Platano"]
print(adiciona(milista))
print(milista)

#Ahora veremos como seria sin modificar la lista original 
def sinmodificar(lista):
    return lista + ["Uva"]

print(sinmodificar(milista))
print(milista)
#Aqui nos tenemos efectos secundarios de modificacion de datos de listas donde el codigo es mas seguro y sigue la inmutabilidad del paradigma 

#Pero y si intentamos usar diccionarios 

#Aqui no hay problema, se mantien inmutables y ademas las unimos correctamente 
a = [1]
b = [2]
print(a+b,a,b)

#Pero como lo hariamos en este caso 
a1 = {"holas":"amigos"}
b1 = {"hola":"Mundo"}

#En este caso si estariamos mutando como efecto secundario al diccionario
a1.update(b1)
print(a1,b1)

#Pero podriamos usar esta tecnica para que no sea mutado a pesar de que no sea completamente inmutable ya que a la hora de usar diccionarios es imposible
#Usaremos copy para poder crear un clon de a asi manteniendo los datos de este y de b seguros y creando un nuevo diccionario a partir de estos dos 
a2 = {"holas":"amigos"}
b2 = {"hola":"Mundo"}
c = a1.copy()
c.update(b2)
print(a1,b2,c)
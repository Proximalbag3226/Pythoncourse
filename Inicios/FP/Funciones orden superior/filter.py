#La funcion flter sirve para filtrar los elementos de un iterable dependiendo de la condicion que le pasemos a la funcion filter
#Solamente va a retornar los elementos que cumplan las condiciones impuestas

#Lista de numeros
numbers = [1,2,3,4,5,6,7,8,9,10]

#Funcion para detectar numeros pares
def pares(numero):
    return numero % 2 == 0

#La funcion filter puede aceptar dos argumentos, que son la funcion a ejecutar y el elemento iterable 
lista_pares = list(filter(pares,numbers))
print(lista_pares)

#Al igual que con map al ser una operaion bastante simple la podemos realizar con lambda funcions
lista_pares2 = list(filter(lambda numero:numero % 2 ==0, numbers))
print(lista_pares2)

#Ejemplo 2
#Retornar nombres que comiencen con la letra A

names = ['Felipe','Amanda','Fernanda','Mario','Ana']

#Funcion  para detectar nombre que empiecen con A

def names_a(nombre):
    return nombre[0] == 'A'

lista_nombresA = list(filter(names_a,names))
print(lista_nombresA)

#Y ahora con lambda funcion

lista_nombresA2 = list(filter(lambda x:x[0] == 'A',names))
print(lista_nombresA2)
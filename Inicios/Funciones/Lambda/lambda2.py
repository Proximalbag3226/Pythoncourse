#Ejercicios sobre las funciones lambda

#Asignamos una variable a la funcion lambda donde va a retornar el segundo elementos de una lista
retorno = lambda x: x[1]
lista = [1,2,3]
print(retorno(lista))

#Podemos tambien reducir la funcion de sumar numeros con lambda functions
sumar = lambda num1,num2: num1+num2
print(sumar(5,8))

#Tambien podemos reescribir la funcion en vez de utiliar los nombres con "x" y "y"
suma2 = lambda x,y: x+y
print(suma2(5,9))
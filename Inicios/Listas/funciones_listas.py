#Aqui estan mas funciones para poder implementar en las listas o cadenas, bastante situacionales pero pueden llegar a ser utiles 

#Strip elimina el exceso de espacios vaciones de una cadena
mensaje = '   Hola como estas  '
sin_espacios = mensaje.strip()
print(sin_espacios)

#Lower cambia todas las letras a minusculas
mensaje = 'HOLA SOY LUIS'
minusculas = mensaje.lower()
print(minusculas)

#Upper cambia todas las letras a mayusculas
mensaje = 'hola como estas'
mayusculas = mensaje.upper()
print(mayusculas)

#Split crea una lista a partir de una cadena 
mensaje = 'Hola que tal'
print(mensaje.split(' '))

#Count nos dice la cantidad de veces que una subcadena aparece en un texto 
mensaje = 'En la calle de mi casa de mi colonia'
print(mensaje.count('mi'))

#Endswhith nos indica si una cadena termina con determinados parametros
mensaje = 'Hola buenos dias'
print(mensaje.endswith('dias'))

#Startswhith nos indica si una cadena comienza con determinados parametros
mensaje = 'Hola buenas tardes'
print(mensaje.startswith('tardes'))

#Capitalize pone en mayusuculas la primer letra de la cadena 
mensaje = 'ola'
print(mensaje.capitalize())

#Find nos sirve para saber si una cadena contiene una subcadena solicitada y nos regresa el indide donde esta comienza 
#De no encontrarse nos regresa -1, es casi lo mismo que index
mensaje = 'ola buenas noshes'
print(mensaje.find('buenas'))

#Index
mensaje = 'ola buenas noshes'
print(mensaje.index('buenas'))

#Isalpha nos indica si en una cadena es de caracteres numericos o alfabeticos
mensaje = 'a1'
print(mensaje.isalpha())

#Isalnum nos indica si la cadena contiene numeros
mensaje = '123abc'
print(mensaje.isalnum())

#Isascii nos indica si la cadena contiene algun elemento en ascii
mensaje = '1234abcd'
print(mensaje.isascii())

#Isdecimal nos indica si la cadena es decimal o no
mensaje = '1.5'
print(mensaje.isdecimal())

#Isdigit nos indica si todos son digitos o no
mensaje = '1234abcd'
print(mensaje.isdigit())

#Para comprobar si una cadena es una palbara reservada de python 
mensaje = 'class'
print(mensaje.isidentifier())

#Para comprobar si hay minusculas
mensaje = 'LUIS'
print(mensaje.islower())

#Para comprobar si hay mayusculas
mensaje = 'luis'
print(mensaje.isupper())

#Replace remplaza una subcadena por otra
mensaje = 'ola wuenas tardes'
print(mensaje.replace("tardes", "noches"))
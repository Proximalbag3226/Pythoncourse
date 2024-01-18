#Las expresiones regulares son patrones de caracteres que se utilizan para poder filtrar cadenas o textos y hacer mas facil si filtrado o manipulacion
#Estas son casi siempre las mismas sin importar el lenguaje con el que estemos trabajando 

#En python nesesitamos importar "er" para trabajar con ellas
import re

#Search nos sirve para saber si una cadena ocurre dentro de otra
r = re.search("si", "Los electrones si son mas pequeos que los protones")
print(r)

#O si no
m = re.search("no", "El te si esta rico")
print(m)

#Estos resulados de la manera en que son retornados pueden ser dificiles de implemetar, usar o simplemente manipular para eso es mejor
#Convertir a boleano

r = bool(re.search("si", "Los electrones si son mas pequeos que los protones"))
print(r)

#O si no
m = bool(re.search("no", "El te si esta rico"))
print(m)

#De esta manera es mejor expresar el resultado, y tambien podemos implementar un if 
if re.search("si", "Los electrones si son mas pequeos que los protones"):
    print("Resultado encontrado")
else:
    print("No se encontro coincidencia")

if re.search("no", "El te si esta rico"):
    print("Resultado encontrado")
else:
    print("No se encontro coincidencia")
    
#Dentro de las expresiones regulares tenemos lo que podemos llamar metacaracteres que son aquellos que dan indicaciones especiales sobre un funcionamiento en particular 
#En este caso empezaremos con el punto (.)

#El punto significa cualquier caracter, ejemplo
r = re.search(r'g.sta', 'me gusta la pizza')
print(r)


r = re.search(r'p.za', 'me gusta la pizza')
print(r)

#Y ahora un ejemplo de la implementacion

import re

# Texto de ejemplo
texto = """
Ejemplo de texto con direcciones de correo electrónico:
juan@example.com
maria@gmail.com
pedro@domain.com
"""

# Definir el patrón de búsqueda para direcciones de correo electrónico
patron_correo = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Buscar todas las direcciones de correo electrónico en el texto
direcciones_correo = re.findall(patron_correo, texto)

# Imprimir las direcciones de correo encontradas
print("Direcciones de correo electrónico encontradas:")
for direccion in direcciones_correo:
    print(direccion)

#Y ahora mas funciones que vienen con las expresiones regulares que nos pueden ayudar a encontrar los valores y caracteres mas facilmente 

#Complemento para este se utiliza el: ^
if re.search(r'N[^ie]c', 'Hola Nico')!=None:
    print("Encontrado")
else:
    print("No encontrado")
    
#Match: para saber si una cadena comienza con una expresion  

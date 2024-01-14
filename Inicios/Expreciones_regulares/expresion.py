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
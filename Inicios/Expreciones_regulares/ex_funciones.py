#Ahora mas expresiones regulares y funciones para las expreiones regulares
import re

#La funcion findall, retorna una lista con todos los match que hizo en la cadena 
encontrados = re.findall(r'c[ao]s', 'El caos lo es todo, univero y oscuridad, caos, hermosa estrella y galaxias cosa complicada es, oh tierra casa mia')
print(encontrados)

#Alternaciones, aqui tenemos opciones de palabras en vez de caracteres 
if re.search('(c|java|python)', 'Yo se js pero prefiero python'):
    print("Sabes dos lenguajes")
else:
    print("Aprende java")

#Split es una funcion que ya habiamos revisado en las listas y sus funciones mas sin embargo tambien se puede utilizar en las expresiones regulares
mensaje = "Este es una prueba de separacion de cadenas"
partes = re.split(r'[ ,]', mensaje)
print(partes)

#Para remplazar al igual que ya habiamos revisado en las listas y sus funciones utilizamos sub
mensaje = "Yo hablo ingles y no soy britanico"
sustituir = re.sub(r'(ingles|britanico)', 'japones', mensaje)
print(sustituir)
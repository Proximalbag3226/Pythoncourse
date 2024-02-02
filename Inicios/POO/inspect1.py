import inspect
import modulo_ejemplo


#Esto va a buscar las clases, funciones y objetos de un modulo, en este caso el que hemos creado
for nombre, datos in inspect.getmembers(modulo_ejemplo):
    if nombre.startswith('__'):
        continue
    print(f"Nombre: {nombre}, datos: {datos}")
    
#Ahora solamente las clases del modulo
for nombre, datos in inspect.getmembers(modulo_ejemplo, inspect.isclass):
    print(F"Clase: {nombre}, datos: {datos}")
    
#Ahora los metodos de una clase
for nombre, datos in inspect.getmembers(modulo_ejemplo.Clase_base, inspect.isfunction):
    print(f"Clase: {nombre}, datos: {datos}")
    
#Tambien podemos obtener la documentacion 
print(modulo_ejemplo.Clase_base.__doc__)

#Obtenemos el codigo fuente de la clase
print(inspect.getsource(modulo_ejemplo.Clase_base))

#Obtenemos el codigo fuente de un metodo 
print(inspect.getsource(modulo_ejemplo.Clase_hija.mi_metodo))

#Obtenemos la firma(parametros) de la funcion 
print(inspect.signature(modulo_ejemplo.mifuncion))

#Obtenemos tambien los argumentos 
def funcion_con_parametros(a, b=10, *args, **kwargs):
    pass

argspec = inspect.getargspec(funcion_con_parametros)
print(argspec)

#Obtemos info de los miembros de un modulo
import math
miembros = inspect.getmembers(math)
print(miembros[:5])




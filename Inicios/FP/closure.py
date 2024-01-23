#los closure son funciones que pueden capturar el ambiente lo que le permite acceder a las variables circundanes aun despues de que la ejecucion de la funcion 
#Haya finalizado En términos más sencillos, un closure es una función interna que puede acceder y recordar las variables de la función externa en la que fue creada, 
#Incluso después de que la función externa haya finalizado su ejecución.

#Ejemplo 

#En esta funcion la parte externa llamada multiplicacion no retorna un valor si no mas bien a la misma funcion interna 
def multiplicacion(x):
    
    #Y en la parte de la funcion interna lo que es retornado si es un valor, para ser mas especificos es el valor "ambiente" ya que captura a x y a y 
    def interna(y):
        return x *y
    return interna

#Creamos un closure
multiplicacion1 = multiplicacion(2)

#Ejecutamos el closure recien creado 
resultado = multiplicacion1(5)
print(resultado)

#Ahora otro ejemplo para poder ver de mejor manera la parte de la toma de las variables del ambiente 
def funcion2():
    x = 1
    def interna2():
        return x
    return interna2

#En esta parte podemos obvervar como el retorno a pesar de que la funcion ya fue ejecutada mantiene su valor en x = 1 guardado en la funcion f2
f2 = funcion2()
assert f2() == 1
print("Todo bien")
print(f2)
print(f2())
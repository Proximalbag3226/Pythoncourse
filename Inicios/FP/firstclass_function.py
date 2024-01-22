#En FP otro concepto de funciones que es importante ademas de las funciones de orden superior y las funciones puras son las funciones de primera clase
#Estas funciones son funciones que pueden ser tratadas como cualquier otro tipo de dato, estas funciones pueden ser pasadas como argumentos o valores de ratorno
#En esta parte son parecidas a las funciones de orden superior, ahora algunos ejemplos de como funcionan 

#Asignadas a variables 
def cuadrado(x):
   return x ** 2 

#Aqui estamos asignando directamente la funcion a una variable 
f = cuadrado
print(f(5))   

#Como argumentos de otras funciones 
def argumento(funcion, valor):
    return funcion(valor)

#Asignamos la funcion cuadrado a otra funcion 
resultado = argumento(cuadrado,5)
print(resultado)

#Podemos retornar funciones en otras funciones 
def obtener_funcion_potencia(exponente):
    def potencia(x):
        return x ** exponente
    return potencia

cuadrado2 = obtener_funcion_potencia(2)
cubo = obtener_funcion_potencia(3)

print(cuadrado(2))
print(cubo(2))

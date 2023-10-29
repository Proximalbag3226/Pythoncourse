#Los argumentos posicionales se utilizan cuando a la funcion en cuestion se van a pasar multiple cantidad de argumentos 
#Es una manera ineficiente estar declarando cada uno de dichos argumentos por lo que se utiliza la palabra reservada "args" para 
#Englobar cada uno de los argumentos que se le van a pasar

#Ejemplo
def suma(*args):
#Y bueno args que tipo de valor es?
    print(type(args))
#Como podemos obvservar es una tupla, lo que python hace es convertir los argumentos que le pasamos a la funcion en una tupla y ejecutar la funcion 
    return sum(args)

resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(f"El resultado es {resultado}")

#Y como se veria de la manera tradicional declaradno cada argumento
def suma1(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    return num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10

resultado1 = suma1(1,2,3,4,5,6,7,8,9,10)
print(f"El resultado con el metodo tradicional es {resultado1}")

#Y si lo queremos hacer sin la funcion de suma 
def suma2(*args):
    resultado = 0
    for element in args:
        resultado += element
    return resultado

resultado2 = suma2(1,2,3,4,5,6,7,8,9,10)
print(f"El resultado2 es {resultado2}")

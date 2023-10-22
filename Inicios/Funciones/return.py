#En este caso veremos la sentencia return que se utiliza de manera en las funciones y su uso es para poder obtner un valor obtenido de una funcion en una variable
#Si podemos ver en los ejemplos diferentes de las funciones que hemos realizado las cosas que realizan las funciones no regresan un tipo de valor solamente
#Se van directamente a la consola, pero esto solamente es un ejemplo teorico, la mayoria de las funciones realizan una accion que retorna algun valor o nada
#Ejemplo

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

resultado = suma(1,3)
print(f"El resultado es {resultado}")

resultado_final = resultado * 2
print(f"El resultado final es {resultado_final}")

#Como podemos ver la funcion no nos imprime directamente un valor si no que nos regresa ese valor almacenado en una variable para que nosotros podamos inteactuar con el 
#Los generators son como lo qyue podriamos decir cuiclos anidados solo que con unas ligeras diferencias, los generetors en vez de iterar directamente 
#Otros cilos o bucles, iteran sobre una funcion que dentro contiene un bucle, esta funcion nos va a devolver el valor del bucle uno a la vez
#Son bastante eficientes en terminos del uso de la memoria

#El ciclo for realiza una iteracion y ahi es donde se ejecuta el generator, cuando el codigo llega a un yield entonces la ejecucion se regresa 
#Hasra el for donde realiaz la operacion nuevamente pero ahora con el valor nuevo del ciclo para volver a ser usado por el for

#Definimos la funcion que realizara la accion de generator
def secuencia(maximo):
    
    #Creamos una variable en 0 que sera nuestro contador
    conteo = 0
    
    #Iniciamos el ciclo while para poder iterar sobre la variable siempre y cuando sea menor que el maximo 
    while conteo < maximo:
        
        #Actualizamos el valor de la variable y utilizamos el yield
        conteo = conteo + 1
        yield conteo

#Y ahora usamos el for para iterar lo que crea el generator
for i in secuencia(10):
    print(i)
    
#Y ahora un ejemplo de uso con las tablas de multiplcar

def tablas_multiplicar(maximo, multiplo):
    contador = 0
    
    while contador < maximo:
        contador = contador +1
        if(contador%multiplo ==0):
            yield contador

for i in tablas_multiplicar(100, 9):
    print(i)        
    
#Podemos simplificar aveces los generators en una sola expresion 
cuadrados = (i**2 for i in range(5))

for n in cuadrados:
    print(n)
#Aqui tenemos un ejemplo de algo bastante curioso que es un diccionario pero en vez de los valores tipicos que conocemos sera con funciones lambda
#Esto es bastante util a la hora de la optimizacion de ciertas tareas ya que ahora al accceder al valor del diccionario con cierta llave
#Esto va a realizar la ejecucion de la lambda function, ejemplo de la optimizacion en un caso con muchos if y elif 

#Tenemos la funcion que esta haciendo de calculadora con las diferentes opciones que tiene, cada una de ellas determinada por un elif 
def calculadora(operacion,a,b):
    if operacion == 'suma':
        return a+b
    elif operacion == 'resta':
        return a-b
    elif operacion == 'multiplicacion':
        return a*b
    elif operacion == 'division':
        if a or b == 0:
            ValueError("El valor de los numeros no puede ser 0")
        else:
            return a/b
        
#Ahora vamos a utlizar el diccionario de funciones lambda para realizar esta tarea de una manera mas eficiente 
def calculadora_lambda(operaciones,a,b):
    
    #Aqui definimos el diccionario con las diferentes opciones y la funcion que esta asiganada a cada llave del mismo 
    return{
        'suma': lambda: a+b,
        'resta': lambda: a-b,
        'multiplicacion': lambda: a*b,
        'division': lambda: a/b
        
        #Aqui tenemos que nos va a retorar la operacion y en caso de no encontrarla regresa un valor None
        }.get(operaciones, lambda:None)()

print(calculadora_lambda('suma', 5,6))

print(calculadora_lambda('resta', 5,6))

print(calculadora_lambda('multiplicacion', 5,6))

print(calculadora_lambda('division', 5,6))
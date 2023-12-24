#Tenemos un array de numeros donde se nos pide encontrar los indices de los numeros que su suma sea el numero pedido 

#Declaramos el array de numeros opciones para encontrar la suma 
array = [4, 7, 2, 8]

#El numero objetivo de la suma
objetivo = 9

#Declaramos un diccionario donde se van a almacenar los numeros y sus indices
map = {}

#Comenzamos la funcion que realizara esta tarea
def suma_objetivo():
    
    #Con un ciclo for iteramos en el array donde uno de las variables iteradoras va a almacenar el valor del numero y otra su indice respectivamente
    for i, n in enumerate(array):
        
        #En la variable resta almacenamos el resultado de la diferencia entre el numero objetivo y el numero iterado actual(n)
        resta = objetivo - n
        
        #Si la resta ya se encuentra en la variable map entonces significa que se encontro una pareja de numeros para la suma
        if resta in map:
            
            #Retorna el diccionario como primer valor el indice del numero compañero y el del iterado actual
            return [map[resta], i]
        
        #Si no se encuentra se agrega al diccionario para tenerlo almacenado para las siguientes iteraciones
        map[n] = i
    
    #Y si no se encuentra la suma con ninguno de los dos numeros entonces la funcion retorna un valor nulo 
    return None

#Ejecutamos la función
resultado = suma_objetivo()

#Imprimimos los resultados 
if resultado is not None:
    print(f"Se encontró una pareja que suma al objetivo en los índices {resultado[0]} y {resultado[1]}.")
else:
    print("No se encontró ninguna pareja que sume al objetivo.")
                
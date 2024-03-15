#Se da una lista con difenteres elementos y se te pide retornar un reverso a esta lista sin utilizar funciones preconstruidas o slicing 

#Creamos una funcion para esto
def rever_lista(list):
    
    #Creamos dos variables que utilizaremos en el ciclo para poder almancenar los valores de la lista 
    incio = 0
    fin  = len(list) - 1
    
    #Iniciamos un ciclo while que continue hasta que inicio sea menor que fin
    while incio < fin:
        
        #Realizamos un remplazo de los valores de la lista para que asi el ultimo quede en el lugar del primero y asi consecutivamente 
        list[incio], list[fin] = list[fin], list[incio]
        
        #Aumentamos o disminuimos el valor de nuestras variables para que se encuentren a la mitad de la lista 
        incio += 1
        fin -= 1
        
    #Retornamos la lista ya con nuestra logica de reversa echa
    return list

#Y verificamos que todo quedo correcto 
print(rever_lista([1,2,3,4,5,6]))
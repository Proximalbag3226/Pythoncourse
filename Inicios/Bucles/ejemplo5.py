#Se da una lista de numeros y se deben retornar los que son  pares
lista = [34,10,23,57,19,2,8,3]

#Creamos un bucle for que recorra toda la lista
for i in lista:
    
    #Con una condicion devolvemos los que son pares y los imprimimos en la consola
    if i%2 == 0:
        print(i)
        
#tambien se puede cambiar por la siguiente 
# if i % 2 != 0:
#      continue 
#    print(i)
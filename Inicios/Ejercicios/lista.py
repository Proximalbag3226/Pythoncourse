#Crearemos varias funciones que nos permitiran interactuar de diferentes maneras con una lista de elementos para esto aplicaremos los metodos usados en las listas

#Creamos la lista de elementos
lista = list()

#Creamos la funcion para interactuar con la lista
def opciones_lista():
    
    #Inicionamos un ciclo while
    while True:
        
        #Imprimimos las opciones disponibles
        print("1.-Crear lista(Agregar elementos a la lista)"
            "\n2.-Insertar elemento"
            "\n3.-Borrar elemento por nombre"
            "\n4.-Buscar por indice"
            "\n5.-Desplegar lista")
        
        #Solicitamos la opcion
        opcion = int(input("Seleccione alguna de las opciones para ejecutar. ").strip())
        
        #En base a la opcion recibida ejecutamos segun corresponda
        if opcion == 1:
            elemento = input("Ingrese el elemento que desea agregar a la lista. ").strip()
            lista.append(elemento)
        elif opcion == 2:
            elemento = input("Ingrese el elemento que desea agregar a la lista. ").strip()
            indice = int(input("Ingrese el indice del elemento que desea agregar a la lista. "))
            lista.insert(indice, elemento)
        elif opcion == 3:
            nombre = input("Ingrese el nombre del elemento que desea eliminar. ").strip()
            lista.remove(nombre)
        elif opcion == 4:
            indice = int(input("Ingrese el indice a buscar. ").strip())
            print(lista[indice])
        elif opcion == 5:
            print(lista)
        else:
            print("Selecciona una opcion correcta")
            continue
        
        #Bloque para continuar o seguir
        continuar = input("¿Desea continuar? s/n ").strip()
        if continuar == "s":
            opciones_lista()
        elif continuar == "n":
            print("Tnega buen dia. ")
            break

#Ejecutamos
opciones_lista()
    


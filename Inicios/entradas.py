#Entradas de datos

#input,con este tipo de entrada de datos se guarda lo dado en unavariable de tipo string 
nombre = input("Digite su nombre:  ")
print(f"Hola {nombre}") 

#Guardar numero en una variable. Por lo anterior mencionado se requiere convertir la variable de tipo string a una variable de tipo integer para hacer operaciones aritmeticas
numero = int(input("Digite su numero: "))
print(f"Hola {numero+1}")

#Tambien se puede hacer con otros tipos de variable
numero =float(input("Digite su numero: "))
print(f"Hola {numero+1.25}")
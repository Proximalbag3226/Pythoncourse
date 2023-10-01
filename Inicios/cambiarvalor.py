#Se realiza un programa que intercambia el valor de dos variables

#Se decalran y se solicitan los valores de las variables
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")

#Intercambiamos la variable
a , b = b, a 

#Imprimimos los nuevos valores
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
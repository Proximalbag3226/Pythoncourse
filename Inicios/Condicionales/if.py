#El condicional "if" que se traduce al español directamente como "si" es utilizado para poder evaluar una condicion que se impone a cierta accion

#Ejemplo de uso al evaluar si un numero ingresado por el usuario es positivo, negativo o 0

numero = float(input("Ingrese un numero: ").strip())

if numero>0:
    print("El numero es positivo")

elif numero == 0:
    print("El numero es 0")

else:
    print("El numero es negativo")
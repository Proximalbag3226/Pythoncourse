#Vamos a ejemplificar el uso de las funciones utilizando programas basicos de aritmetica simple contenido dentro de funciones, asi como en la calculadora

#Funcion de suma
def suma(numero1, numero2):
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")

#Funcion de resta
def restar(numero1, numero2):
    resultado = numero1 - numero2
    print(f"El resultado de la restar es: {resultado}")
    
#Funcion de multiplicacion
def multiplica(numero1, numero2):
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicacion es: {resultado}")
    
#Funcion de division en donde tambien incluimos una condicion para la division entre 0   
def division(numero1, numero2):
    if numero2 !=0:
        resultado = numero1 / numero2
        print(f"El resultado de la division es {resultado}")
    else:
        print("No se puede dividir entre 0")
        
#Llamamos a una de las funciones, tu puedes llamar a cualquiera y cambiar sus parametros

suma(5,6)
restar(5,6)
multiplica(5,6)
division(5,6)


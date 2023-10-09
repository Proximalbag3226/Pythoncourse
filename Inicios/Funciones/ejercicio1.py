#Es la misma calculadora de la carpeta genral y en esta utilizamos funcuiones

#Definimos las funciones que utilizaremos en la calculadora
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else: 
        return "No se puede dividir entre 0"

#Ahora definiremos una nueva funcion llamada calculadora para ejecutar toda la logica y la entrada de datos
def calculadora():  
    
#Utilizaremos un bucle while para que la calculadora nos pida que ingresemos la operacion aritmetica que deseamos hacer
    while True:
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")

#Con una entrada de datos de tipo input elegimos el numero de operacion lo guaramos en la variable operacion, ademas de pedir los numeros para calcular las operaciones
        operacion = input("Elige un numero de operacion ").strip()
        num1 = float(input("Ingresa el primer numero ").strip())
        num2 = float(input("Ingresa el segundo numero ").strip())

#En esta parte nos dedicaremos a llamar a las diferentes funciones dado el caso que se haya seleccionado dependiendo de la variable operacion 
        if operacion == "1":
            resultado = sumar(num1, num2)
                
        elif operacion == "2":
            resultado = restar(num1, num2)

        elif operacion == "3":
            resultado = multiplicar(num1, num2)

        elif operacion == "4":
            resultado = dividir(num1, num2)
#Em casp de que no se haya elegido un numero de operacion correcto desplegaremos un mensaje de error
        else:
            print("Selecciona una opcion correcta")
            continue

#Y a continuacion el resultado de la operacion sera desplegado 
        print(f"El resultado de la operacion es: {resultado}")

#Ademas contaremos con la opcion de continar calculando otras operaciones o de salir de la calculadora
        continuar = input("Desea continuar (s/n)? ").strip()
        if continuar == "s":
            calculadora()
        elif continuar == "n":
            print("Tenga buen dia")
            break
        
#Y por ultimo vamos a llamar a la funcion calculadora
calculadora()
    
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
    
def calculadora():  
    while True:
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")

        operacion = input("Elige un numero de operacion ").strip()
        num1 = float(input("Ingresa el primer numero ").strip())
        num2 = float(input("Ingresa el segundo numero ").strip())

        if operacion == "1":
            resultado = sumar(num1, num2)
                
        elif operacion == "2":
            resultado = restar(num1, num2)

        elif operacion == "3":
            resultado = multiplicar(num1, num2)

        elif operacion == "4":
            resultado = dividir(num1, num2)
        else:
            print("Selecciona una opcion correcta")
            continue
        
        print(f"El resultado de la operacion es: {resultado}")

        continuar = input("Desea continuar (s/n)? ").strip()
        if continuar == "s":
            calculadora()
        elif continuar == "n":
            print("Tenga buen dia")
            break
calculadora()
    
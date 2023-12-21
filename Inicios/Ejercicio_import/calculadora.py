import Aritmeticas.operacione_basicas as ob
import Aritmeticas.operaciones_avanzadas as oa
def calculadora():
    while True:
        print("1.-Suma")
        print("2.-Resta")
        print("3.-Multiplicacion")
        print("4.-Division")
        opcion = input("Eligue una opcion ").strip() 
        num1 = float(input("Ingrese el primer numero ").strip())
        num2 = float(input("Ingrese el segundo numero ").strip())
        
        if opcion == "1":
            resultado = ob.suma(num1, num2)
            
        elif opcion == "2":
            resultado = ob.resta(num1, num2)
        
        elif opcion == "3":
            resultado = oa.multiplicar(num1, num2)
            
        elif opcion == "4":
            resultado = oa.dividir(num1, num2)
            
        else:
            print("Selecciones una opcion correcta")
            continue
        
        print(f"El resultado es {resultado}")
    
        continuar = input("Desea continuar (s/n)? ").strip()
        if continuar == "s":
            calculadora()
        elif continuar == "n":
            print("Tenga buen dia")
            break
        
calculadora()   
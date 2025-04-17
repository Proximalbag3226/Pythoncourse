#Vamos a realizar un programa que resuleva calculos de longitud parametrica, para ello vamos a utilizar la formula que ya conocemos:
#Seria la integral de la raiz de la suma de las derivadas con respecto a x,y,z (dependiendo de las dimensiones de nuestra curva) elevadas al cuadrado

#Importamos las librerias nesesarias
from sympy import Symbol, integrate, sympify, sqrt

#Colocamos la parametrizacion de forma simbolica
t = Symbol("t")

#Construimos nuestra funcion que nos va a permitir derivar 
def derivadas(*funciones):
    return tuple(f.diff(t) for f in funciones)

#Y otra funcion que nos va a permitir integrar los muchos diferenciales de longitud de la curva
def integral(a, b, *derivadas):
    suma_cuadrados = sum(d**2 for d in derivadas)
    res = integrate(sqrt(suma_cuadrados), (t, a, b))
    return res.evalf()

#El menu principal
while True:
    print("\nBienvenido a la calculadora de longitud parametrica")
    variables = input("¿Su función tiene 2 o 3 dimensiones? (2/3): ").strip()
    
    if variables == "2":
        entrada_x = input("Ingresa tu función x(t): ")
        entrada_y = input("Ingresa tu función y(t): ")
        
        fx = sympify(entrada_x)
        fy = sympify(entrada_y)
        
        a = float(input("Ingresa el límite de integración inferior: "))
        b = float(input("Ingresa el límite de integración superior: "))
        if a>b:
            print("Ingrese limites de integracion validos e intente de nuevo. ")
            break
        elif a == b:
            print("Los limites de integracion deben de ser diferentes, intente de nuevo. ")
            break
        
        dx, dy = derivadas(fx, fy)
        longitud = integral(a, b, dx, dy)
        
        print(f"La longitud paramétrica es de: {longitud}")
        
    elif variables == "3":
        entrada_x = input("Ingresa tu función x(t): ")
        entrada_y = input("Ingresa tu función y(t): ")
        entrada_z = input("Ingresa tu función z(t): ")
        
        fx = sympify(entrada_x)
        fy = sympify(entrada_y)
        fz = sympify(entrada_z)
        
        a = float(input("Ingresa el límite de integración inferior: "))
        b = float(input("Ingresa el límite de integración superior: "))
        
        dx, dy, dz = derivadas(fx, fy, fz)
        longitud = integral(a, b, dx, dy, dz)
        
        print(f"La longitud paramétrica es de: {longitud}")
        
    else:
        print("Selecciona una opción correcta (2 o 3).")
        continue

    continuar = input("¿Desea continuar? (s/n): ").strip().lower()
    if continuar != "s":
        print("Tenga un buen día.")
        break
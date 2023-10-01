#Crear un programa que determine el orden de mayor a menor de 3 numeros solicitados

num1 = float(input("Ingrese el primer numero ").strip())
num2 = float(input("Ingrese el segundo numero ").strip())
num3 = float(input("Ingrese el tercero numero ").strip())

if num1>num2 and num2>num3:
    print(f"El numero mas grande es {num1}, le sigue {num2} y por ultimo {num3}")
elif num1>num2 and num3>num2:
    print(f"El numero mas grande es {num1}, le sigue {num3} y por ultimo {num2}")
elif num2>num1 and num1>num3:
    print(f"El numero mas grande es {num2}, le sigue {num1} y por ultimo {num3}")
elif num2>num3 and num3>num1:
    print(f"El numero mas grande es {num2}, le sigue {num3} y por ultimo {num1}")
elif num3>num1 and num1>num2:
    print(f"El numero mas grande es {num3}, le sigue {num1} y por ultimo {num2}")
elif num3>num2 and num2>num1:
    print(f"El numero mas grande es {num3}, le sigue {num2} y por ultimo {num1}")
else:
    print("Todos los numeros son iguales")
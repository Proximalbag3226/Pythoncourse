#Hacer un programa que reciba dos numeros y que identifque si ambos son pares o si uno de ellos lo es
num1 = int(input("Ingrese el primer numero ").strip())
num2 = int(input("Ingrese el segundo numero ").strip())

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos numeros son pares")
elif num1 % 2 == 0 and num2 % 2 !=0:
    print("El numero dos no es par")
elif num1 % 2 != 0 and num2 % 2 ==0:
    print("El numero 1 no es par ")
else:
    print("Ninguno de los dos es par")
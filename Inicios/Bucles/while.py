#EL bucle while, en el bucle while es conocido por tener un numero indeterminado de iteraciones esto a partir de que se cumpla una condicion
#Si esta condicion se cumple las iteraciones seguiran de forma indeterminada

import math

numero = int(input("Ingrese un nuermo para obtener su raiz cuadrada ").strip())

while numero<0:
    print("Error el numero debe ser un numero positivo")
    numero = int(input("Ingrese un nuermo para obtener su raiz cuadrada ").strip())
print(f"Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")

#Tambien podemos especificar las iteraciones a realizar con la variable iteradora (i)
i = 0
while i<10:
    print(i)
    i = i + 1
#tambien podemos modificar con el operador += o -=

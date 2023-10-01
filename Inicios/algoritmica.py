#Vamos a transformar la ecuacion ((a^3)(b^2-2ac))/2b

#Definimos y pedimos los valores para las diferentes variables
a = float(input("Ingresa el valor de a").strip())
b = float(input("Ingresa el valor de b").strip())
c = float(input("Ingresa el valor de c").strip())

#Transformamos la ecucacion a operadores aritmeticos
resultado = (a**3 * (b**2-2*a*c))/(2*b)

#Imprimimos el resultado
print(f"El resultado es {resultado}")    
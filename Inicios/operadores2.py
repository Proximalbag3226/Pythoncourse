#Vamos a probar la veracidad de una operacion con diferentes tipos de operadores tanto matematicos como tambien logicos
#Operacion a verificar: ((3 + 5 x 8))<3 and ((-6/3 x 4)+2<2) or (a>b)

#Declaramos y solicitamos nuestras variables

a = int(input("Ingrese el valor de a ").strip())
b = int(input("Ingrese el valor de b ").strip())

#Convertimos la operacion a operadores ariteticos 
resultado = ((3 + 5 * 8))<3 and ((-6/3 * 4)+2<2) or (a>b)

#Imprimimos el resultado
print(f"Esta operacion es: {resultado}")


#Esto tambien se puede realizar utilizando valor de tipo flotante en vez de int
#Condicinales combinados 

edad = int(input("Escirba su edad: ").strip())

if edad>0:
    print("Edad correcta")
    if edad>18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("Edad incorrecta")
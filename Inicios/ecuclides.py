#Pasar el algoritmo de eculides a python

a = int(input("Ingrese el valor del primer numero: ").strip())
b = int(input("Ingrese el valor del segundo numero: ").strip())


def  euclides(a, b):
    while True:
        resto = a % b
        if resto == 0:
            return(b)   
        else:
            a = b
            b = resto
print (euclides(a, b))
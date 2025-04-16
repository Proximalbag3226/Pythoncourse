#Vamos a realizar un programa que resuleva calculos de longitud parametrica, para ello vamos a utilizar la formula que ya conocemos:
#Seria la integral de la raiz de la suma de las derivadas con respecto a x,y,z (dependiendo de las dimensiones de nuestra curva) elevadas al cuadrado

import sympy as sp
from sympy import Symbol, integrate
x = Symbol("x")
y = Symbol("y")
z = Symbol("z")
t = Symbol("t")

x = sp.Symbol('x')
entrada = input("Ingresa la función: ")
fx = sp.sympify(entrada)

derivada = fx.diff(x)
print("Derivada:", derivada)

def derivadas(x1,y1,z1):
    dx1 = x1.diff(x)
    dy1 = y1.diff(y)
    dz1 = z1.diff(z)
    return dx1, dy1, dz1

def integral(a,b,funcion):
    res = sqr(integrate(funcion,(t,a,b)))

while(True):
    print("Bienvenido a la calculadora de longitud de arco")
    variables = input("¿Su funcion tiene 2 o 3 dimensiones?")
    if variables == "2":
        break
    elif variables == "3":
        break

#Realizar un programa que capture el radio de un circulo y devuelva su area y su circunferencia 

#Imporatmos la libreriia math para tener acceso al valor de pi
import math 

#Solicitamos el valor del radio
radio = float(input("Ingrese el valor del radio del la circunferencia ").strip())

#Aplicamos la formula del area del circulo al valor del radio
area = math.pi * radio**2

#Aplicamos la formula de la longitud de la circunferencia al valor del radio
circunferencia = 2 * math.pi * radio

print(f"El area del circulo es de: {area}, y la longitud de su circunferencia de: {circunferencia}")
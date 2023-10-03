#Aplicaremos los bucles for para la interfaz grafica donde podremos obvservar mejor su funcionamiento
import turtle

#Creamos la ventana de la interfaz grafica y cambiamos su color de fondo
ventana = turtle.Screen()
ventana.bgcolor("white")

#Creamos la flecha que se va a mover en la ventana
flecha = turtle.Turtle()
flecha.speed(1)

#Ahora usando un bucle for dibujaremos un cuadrado pasando las instrucciones a la flecha
for i in range(4):
    flecha.forward(100)
    flecha.right(90)

#Y el resultado final es un cuadrado dibujado
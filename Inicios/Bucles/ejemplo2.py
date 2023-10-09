#Al igual que en el primer ejemplo mostrado para utilizar los bucles for dentro de la interfaz grafica ahora realizaremos otra figura 
import turtle

#Creamos la ventana de la interfaz grafica
ventana = turtle.Screen()
ventana.bgcolor("white")

#Creamos la flecha que dibujara nuestra figura
flecha = turtle.Turtle()
flecha.speed(1)

#Con el bucle for hacemos iteraciones de las instrucciones para crear nuestra figura dentro de la ventana
for i in range(5):
    flecha.forward(200)
    flecha.right(144)
    
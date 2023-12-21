import turtle
import random
 
ventana = turtle.Screen()
ventana.bgcolor("black")
flecha = turtle.Turtle()
flecha.speed(0)
flecha.color("white")
ventana.title("Estrellas")

def estrellas():
    for i in range(5):
        flecha.fd(10)
        flecha.right(144)
        
estrellas()
flecha.begin_fill()
flecha.end_fill()
flecha.hideturtle()
ventana.exitonclick()
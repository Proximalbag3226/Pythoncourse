#En este ejemplo mostraremos de forma grafica del ejemplo anterior

#Importaremos las librerias que vamos a utilizar
import random
import turtle

ventana = turtle.Screen()
ventana.bgcolor("Lightblue")
ventana.title("Carrera de caracoles")
ventana.setup(width=800, height=600)

caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("Red")
caracol1.penup()
caracol1.goto(-300,100) 



ventana.exitonclick()
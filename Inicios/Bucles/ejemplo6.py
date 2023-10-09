#En este ejemplo modificaremos conla sentencia continue el ejemplo 4 para que solamente se avanze en la carrera si el numero obtenido es un impar

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

caracol2 =  turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("Blue")
caracol2.penup()
caracol2.goto(-300,200)

meta = 300

#Lina de meta
meta_line =  turtle.Turtle()
meta_line.penup()
meta_line.goto(meta, 250)
meta_line.pendown()
meta_line.goto(meta, -150)
meta_line.hideturtle()

while True:         
    avance_caracol_1 = random.randint(1, 20)
    avance_caracol_2 = random.randint(1, 20)
     
    if avance_caracol_1 % 2 != 0 or avance_caracol_2 % 2 != 0:
        continue         
    caracol1.forward(avance_caracol_1)
    caracol2.forward(avance_caracol_2)
    print(f"El caracol 1 avanza {avance_caracol_1} y lleva una distancia de {caracol1.xcor()}")  
    print(f"El caracol 2 avanza {avance_caracol_2} y lleva una distancia de {caracol2.xcor}")
    print("----------------------------------------------------------------")
    
    if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
        break

if caracol1.xcor() > caracol2.xcor():
    print("El caracol 1 es el ganador")
elif caracol2.xcor() > caracol1.xcor():
    print("El caracol 2 es el gandor")
else:
    print("Es un empate")

ventana.exitonclick()
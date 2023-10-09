#En este ejemplo mostraremos de forma grafica del ejemplo anterior

#Importaremos las librerias que vamos a utilizar
import random
import turtle

#Creamos y personalizamos la ventana del entorno grafico
ventana = turtle.Screen()
ventana.bgcolor("Lightblue")
ventana.title("Carrera de caracoles")
ventana.setup(width=800, height=600)

#Creamos los graficos para los caracoles y les damos posicion y personalizacion
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

#Definimos la meta
meta = 300

#Pasamos la logica del ejemplo anterior
while True:     
    avance_caracol_1 = random.randint(1, 20)
    avance_caracol_2 = random.randint(1, 20)         
    caracol1.forward(avance_caracol_1)
    caracol2.forward(avance_caracol_2)
    
    #Utilizamos el metodo xcor para obtener las coordenadas en el eje x del caracol
    print(f"El caracol 1 avanza{avance_caracol_1} y lleva una distancia de {caracol1.xcor()}")  
    print(f"El caracol 2 avanza{avance_caracol_2} y lleva una distancia de {caracol2.xcor}")
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
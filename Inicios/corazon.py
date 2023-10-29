import turtle as t
from math import cos, sin

t.tracer(2)
t.bgcolor('black')
t.color('red')

def coraX(n):
    x = 15*sin(n)**3
    return x

def coraY(n):
    x = 12*cos(n)-5*cos(2*n)-2*cos(3*n)-cos(4*n)
    return x

for i in range(1000):
    t.goto(coraX(i)*10, coraY(i)*10)
    t.goto(0,0)

t.exitonclick()
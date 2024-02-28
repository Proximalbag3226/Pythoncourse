#Ahora comenzaremos con una parte muy importante del desarrollo de software, el testing, creo que el concepto de testing como tal no es dificl de entender ya que como 
#Su nombre lo indica esto se trata de realizar pruebas para el programa que realizaste para ber si se comporta de la manera esperada y que de los resultados esperados para 
#Los requerimientos del problema a resolver por tanto essta es una de las partes funamentales del desrrollo ya que es la parte deonde nos podemos dar cuenta de 
#Los errores que puede llegar a tener nuestro software y corregirlos para un funcionamiento mas eficiente y adecuado, aqui te explicare los diferntes tipos de pruebas 
#O por lo menos algunas de ellas, aunque tambien se tiene que llevar una bitacora de pruebas y un reporte de cada una de ellas para poder llevar un registro de cada una
#Y de los esenarios a evaluar para poner a prueba el software, pero de mientras un ejemplo sencillo para introduccion 
from math import pi

#definimos una funcion 
def area(radio):
    area =  pi * (radio**2)
    return area

#Version con la excepcion de ValueError
def area2(radio):
    #Verificamos que se cumpla la condicion dada
    if radio < 0:
        raise ValueError ("El radio debe ser mayor a 0")
    area = pi * (radio**2)
    print(area)
    return area

#Pero esta es una forma primitiva de probar la funcion, funciona pero no es lo optimo, vamos a probarla 
#Creamos una lista de valores que vamos a pasar a la funcion para ver con cuales truena 
valores = [1,2,3,4,5,6,0,-1,2+3j, False, "Zy", [1,2,3]]

#Recorremos los valores evaluando cada uno de ellos para la funcion 
for i in valores:
    try: areac = area2(i)
    except Exception as e: print(e)
    
#Al observar como funciona el programa con los difertenres tipos de datos que pasamos podemos identificaer diferentes errores por ejemplo al pasar boleean, lista, string
#Pero esto podria ser mejor ya que en python podemos seguir un protocolo para la creacion de pruebas, el cual consiste en realizarlas en otro archivo para las unit test

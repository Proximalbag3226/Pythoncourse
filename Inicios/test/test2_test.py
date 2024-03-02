#Ahora vamos a utilizar la segunda funcion que creamos en el test1 para poder utilizar otro tipo de test, el assertRaises
from test1 import *
from math import pi
import unittest

class Test_area(unittest.TestCase):
    def test_negativo(self):
        print("-----Test de valores negativos-----")
    
    #Indicamos el tipo de exepcion, la funcion y el valor que sabemos debe generar la exepcion 
        self.assertRaises(ValueError, area2, -1)
        #Lo que hara esta funcion es verficar el funcionamiento de las exepciones que incluimos en la funcion y su correcto funcionamiento
        

    #Ahora vamos a probar otro tipo de test donde vamos a verificar el tipo correcto de dato que nesesitamos por parametro 
    def test_tipos(self):
        #El tipo de exepcion a utilizar debe ser de TypeError y vamos a realizar una prueba para cada tipo que sabemos que no es compatible con 
        #El parametro de la funcion que estamos testeando 
        print("------Test de tipos no compatibles------")
        self.assertRaises(TypeError, area2, True)
        self.assertRaises(TypeError, area2, 'hola')
        self.assertRaises(TypeError, area2, 2 + 3j)
        
        #Y como podremos ver no se detecta la exepcion por lo que este test nos deberia llevar a modificar nuestro codigo para implementar eso 
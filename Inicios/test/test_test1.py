#Aqui vamos a crear el unit test
#Para ejecutar el test ponemos en consola !python -m unittest nobre_del_test
#Importamos unittest
import unittest

#Importamos el metodo a usar y lo extra
from test1 import area
from math import pi

#Creamos una clase que hereda TestCase 
class TestArea(unittest.TestCase):
    
    #Definimos el metodo donde vamos a llevar a cabo el test y este debe inicar con test 
    def test_area(self):
        print("------test valores de resultado------")
        
        #Vamos a hacer un test para un valor que ya conocemos el resultado
        self.assertEqual(area(1), pi)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(3), pi*(3**2))
        
        #Ahora simularemos que recibimos un valor incorrecto 
        self.assertEqual(area(3.1), pi*(3**2))
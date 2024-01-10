#Las clases internas son un concepto que e bastante sencillo como lo es que simplemente tenemos una clase definida dentro de otra clase
#Dicho concepto nos pueden ayudar a organizar nuestro codigo, la clase principal se puede ayudar en las clases internas para diversas funciones
#Las clases internas pueden tener acceso a los atributos de la externa y viceversa, el principal uso como ya se menciono es organizar y 
#Moduralizar el codigo o limitar el alcanze de ciertas clases a una parte especifica del codigo 

#Ejemplo
class Externa:
    
    #Creamos los atributos de instancia en la clase externa
    def __init__(self, x):
        self.x = x
        self.interna = self.Interna()
    
    #Ahora un metodo para imprimir el valor de x en la clase externa 
    def imprimir_x(self):
        print(f"X esta en la clase externa y vale {self.x}")
        
    #Creamos la clase interna dentro
    class Interna:
        
        #Igualmente sis atributos de instancia 
        def __init__(self):
            self.y = 10
         
        #Y un metodo para imrimir y dentro de la interna   
        def imprimir_y(self):
            print(f"Y esta en la clase interna y vale {self.y}")

externo = Externa(10)
externo.imprimir_x()
externo.interna.imprimir_y()
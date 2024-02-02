#Este es el modulo de ejemplo que se utilizara para el archivo de inspect 

def mifuncion(parametro1, parametro2="Texto"):
    """Esta es una funcion"""
    valor  = parametro1 * 3
    print(f"Hola {parametro2}")
    return valor

class Clase_base(object):
    """Ejemplo de una clase cualquiera"""
    
    def __init__(self, p_nombre):
        self.nombre = p_nombre
        
    def getNombre(self):
        #Retornamos el nombre de la instancia
        return self.nombre

objeto1 = Clase_base("Primer objeto")

class Clase_hija(Clase_base):
    """Clase hija"""   
    
    def mi_metodo(self):
        x= 5
    
    def getNombre(self):
        return 'clase hija' + self.nombre
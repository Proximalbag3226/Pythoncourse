#Veremos unos de lo pilares de la poo el encapsulamiento

class Pikachu:
    
    tipo = "Electrico"
    
    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.voltaje_max = voltaje_max
        self.amperaje_max = amperaje_max
        self.color = color
        
    def atacar(self):
        print(f"{self.nombre} ataca y realiza {self.nivel/4} de daño")
        
Pikachu_1 = Pikachu()

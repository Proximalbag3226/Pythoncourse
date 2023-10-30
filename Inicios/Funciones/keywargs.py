#los key args funcionan como un diccionario ya que pasan los arguemtnso asi como los posicionales pero asignando una llave a cada uno de los argumentos 

def conectarBD(**kwargs):
#Como podemos ver es de tipo diccionario
    print(type(kwargs))
    print(kwargs)
    nombre = kwargs.get('nombre', "Default")
    user = kwargs['usuario']
    password = kwargs['password']
    port = kwargs['port']
    dir_bd = kwargs['dir_bd']
    print(f"Conectando con la base de datos {nombre} con el usuario {user} la clave {password} el puerto {port} y la dirección {dir_bd}")
    
#Vamos a llamar pasando los parametros como si fueran diccionarios
conectarBD(usuario = "root", 
           password = "1234", 
           port = 3000,
           dir_bd = "10.25.47.3")
#Los context manager al igual que el manejo de las expeciones son una manera de garantizar que una fraccionde codigo se ejecute si o si dado que una parte del codigo
#"Truene" y veremos como crearlos y utilizarlos aunque como en si su uso es vastante parecido al manejo de exepciones con las sentencias ya vistas
#Como son las condicionales y los try y exept 

#Creamos un ejemplo de codigo que se ejecuta y por algunmotivo truena y lo manejamos con las exepciones correctas
a = 5
b =1 

archivo = open('mi archivo.txt', 'w')
archivo.write('Hola tonotos')

#Creamos una exepcion que no nos deje llegar al close
r = a/b
archivo.close()

#Y solucionamos con exepciones
a = 5 
b = 3
archivo.open()
try:
    archivo.write("Hola tonotos x2")

finally:
    archivo.close()
    
#Ahora menejemos el error con un context manager

class Cm():
    
    #En la inizializacion recibimos el archivo y abrir que es su modo de abertura 
    def __init__(self, archivo, abrir):
        self.archivo = open(archivo, abrir)
    
    #Aqui esta el codigo de entrada que lo identificamos por el print y retornamos el archivo abierto
    def __enter__(self):
        print("En la entrada")
        return self.archivo
    
    #Para la salida tenemos una impresion de la salida y el archivo cerrado, en este caso esta parte del codigo es lo que queremos que simpre se ejecute
    def __exit__(self, type, value, traceback):
        print("En la salida")
        
        #Obttenemos la info de la exepcion 
        print("type: " + type)
        print("value: " + value)
        print("tracebacktrace" + traceback)
        
        #Comenzamos el manejo de errores
        if type == ZeroDivisionError:
            print("No dividir entre 0")
            return True
        
        self.archivo.close()
        
#Pomemos el context manager
with Cm('archivo.txt', 'w') as archivo:
    print("Aqui estamos en el context manager")
    archivo.write("Holas")
    a = 5/0
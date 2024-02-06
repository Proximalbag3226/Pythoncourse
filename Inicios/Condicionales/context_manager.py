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
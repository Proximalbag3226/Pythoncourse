#Los loggers son parte del modulo integrado logging, que nos porporciona una forma de registrar mensajes y eventos durante la ejecución de nuestro
#Programa, los loggers nos son utiles para poder registrar la informacion durante la ejecución y por lo tanto facilita la depuracion de codigo 
#El seguimiento de errores y tambien nos ayudan a comprender el flujo del programa, los loggers se utilizan en jerarquia de nombres que fallas 
#Como son las siguientes: Notset = 0, Debug = 10, Info = 20, Warn = 30, Error = 40 y Critical o Fatal = 50

#Tenemos un concepto que conocemos como formateador, este coloca al log la informacion que da el contexto (archivo, linea, metod, hilo y proceso)
#Otro de las partes importantes a aprender es el handeler, esta es la parte en donde obtenemos los datos, se puede atraves de la consola como siempre de toda la vida
#Y tambien por email con SMTPhandler, estos dos son los mas comunes pero hay mas, estos los puedes revisar en la documentacion del handler de python 
#El handler necesita de 2 campos, el formateador y el nivel(ese que esta alla arriba con numeros), el formateador va a pasar el mensaje y el nivel
#Especifica lo demas.

#Para obtener un logge tenemos que crearlos primero con el metodo getlogger()
#El logger tiene 3 campos:
#Propagacion: Esto es como la herencia dentro de poo, ya que es lo que decide si el log se debe de propagar al padre del logger 
#Nivel: Esto como ya vimos anteriormente se utiliza para filtar logs menos importantes 
#Handler: Y por ultimo esto es la lista de handlers a los que sera enviado el  log, esto es importante ya que podemos tener mas de un handler 
#Por ejemplo uno que envie a consola los casos de debug y otro que envie un email en caso de ctritical o fatal 

#El "Idenrtificador" del logger es en un nombre y cada que lo usemos obtendremos el mismo objeto 

#Ahora explicaremos el sistema jerarquico de los loggers, hasta arriba tenemos el root logger o logging.root, su nivel es de warm, los logger mas abajos a este 
#Nivel van a ser ignorados, por default los loggers que creemos estaran como hijos de root 

#Tenemos un concepto mas, el nivel efectivo. Este es el mismo que el nivel con la exepción de que no sea Nonset
#Si creamos un loger y lo declaramos con Notset este buscara en sus antepasados el nivel mas cercano que no sea Nonset
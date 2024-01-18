#La programacion funcional al igual que la programacion orientada(POO) a objetos es un paradigma que trata de abordar la computacion como la evaluación 
#De funciones matematicas y evita el cambio de estado y las variables prefiriendo por sobre todo estructuras de datos que sean inmutables 
#Este es el motivo de que se utilizen tanto las tuplas en este paradigma, ademas de expresiones sin efectos secundarios, esto ultimo hace referencia 
#A que las funciones que sean creadas en base a la funcionalidad no deben ir mas haya del resultado que retornan es decir que no deben de modificar
#El ambito local mas alla de si mismas y su resultado.
#Como en la POO aqui tambien tenemos ciertos "Pilares" o mas bien caracteristicas las cuales seran mencionadas a continuacion:

#Funciones puras: Estas funciones son tales que dado el mismo conjunto de datos va a retornar siempre el mismo resultado y que ademas cumplira la 
#Condicion de no afectar nada afuera de ella misma, aqui un pequeño ejemplo de diferencia:

#Esta es una funcion impura ya que altera el comportamiento externo a ella
numero = 5
def funcion_impura():
    global numero
    numero =+ 5
    return numero

#Esta función es pura, ya que solo depende de sus parámetros y no modifica nada fuera de su ámbito
def funcion_pura(x, y):
    return x + y


#Inmutabilidad: Esta es una parte interesante de la prigramacion funcional(FP) y hace referencia a que una vez creados los datos que van a ser 
#Utilizados estos no pueden ser modificados ni alterados de ninguna manera, por eso mismo el uso de tuplas, en vez de ello se crean nuevos datos

#Expresiones y evaluaciones: La atencion debe ser centrada en la evaluacion de las expresiones y no como tal en su ejecucion de las instrucciones 
#Dichas expresiones deben ser evaluadas para cumplir con no producir efectos secundarios 

#Funciones de orden superior: Como anteriormente se pudo revisar en los tipos de funciones tenemos las de orden superior (Explicadas en la carpeta de Funciones/funciones orden superior)
#Estas van a ser de suma importancia en este paradigma ya que son muy utilizadas para el trtamiento de otras funciones ya que pueden recibirlas como argumentos 

#Recursividad: Aqui en ves de tener ciclos iterativos se prefiere utilizar la recursividad y dividir los problemas en subproblemas e ir resolviendo recursivamente 

#Programar declarando: Eh aqui un caso especial ya que a diferencia de como estamos acostumbrados este punto refiere a que en lugar de describir como hacer algo
#Se prefiere describir que se debe hacer sin especificar como se debe de realizar ya que la FP se centra en explicar la logica de la computacion sin especificar
#La secuencia de comandos detallada 

#Evaluación floja: Se evalúan solo las expresiones que son necesarias para producir un resultado y lo demas alv 

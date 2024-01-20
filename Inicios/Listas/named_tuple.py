#A diferencia de su hermana la tupla que so bastante parecidas entre si eso si se debe mencionar esta nos permite trabajar co tuplas las cuales sus elementos tienen 
#Nombres en particular, se podria decir que es como una combinacion entre los diccionarios y las tuplas ya que al igual que en los diccionarios podemos acceder 
#Por indices y por los nombres de los campos, estas pueden ser bastante utiles en la programacion funional(FP)

#Importamos los modulos nesesarios 
from collections import namedtuple

#Creamos una namedtuple
punto =  namedtuple('Punto', ['x', 'y']) 

#Creamos una instancia de la namedtuple 
p1 = punto(x=1, y=2)
p2 = punto(x=5, y=3)

#Accedemos a los elementos por indice
print(p1[0], p1[1])  

#Y tambien podemos acceder por medio del nombre 
print(p1.x, p1.y)

#Como se menciono al principio las namedtuple y los diccionarios son parecidos y por lo tanto podemos convertir uno en otro     
diccionario1 = p1._asdict()
print(diccionario1)

#Es importante rocrdar que siguen siendo tuplas pero con la diferencia que son una estructura de datos con informacion fija pero nombres significativos 
#Son mas utiles que los diccionarios y mas legibles que las tuplas normales y cabe recordar asi mismo que alser tuplas tambien son estructura de datos inmutables
#Y ahora algunos metodos y funciones que podemos utilizar 

#Con fields podemos imprimir el nombre de los campos
print(p1._fields)

#Para "remplazar" un contenido y remplazo entre comillas porque en realidad sucede cuando utilizamos el metodo replace es que els sistema crea una nueva tupla en memoria 
#Utilizando como plantilla la tupla anterior, asi que mas que remplazo podriamos decir que en realidad es una clonacion en memoria, eliminamos una y creamos una nueva 
p2 = p2._replace(x=4)
print(p2)

#Tambien podemos crear la tupla es usando make 
p3 = punto._make([2,4])
print(p3)
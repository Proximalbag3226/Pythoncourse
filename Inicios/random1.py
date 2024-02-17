#Vamos a trabajar con random para la creacion de numeros aleatorios, random creo ya lo eh usado antes para otros codigos aqui pero no como tal explicarlo para que lo uses
#Random es un modulo ya nativo de python por lo cuao no nesesita su instalacion o algo asi simplemente la importacion del modulo dentro del codigo
#Randon se encarga de la generacion de numeros pseudoaleatorios para varias distribuciones, en la teoria este modulo utiliza diferentes mtodologias y formas para hacerlo
#Posible el echo de calcular esos numeros, para los numeros enteros hay una seleccion uniforme dentro de un rango establecido, para las secuencias se utiliza 
#Una seleccion uniforme de un elemento aleatorio, una funcion para generar permutaciones aleatorias de la lista y otra funcion para el muestreo aleatorio sin remplazo
#Para los numeros reales el modulo tiene mas formas de tratarlo ya que existen diferentes formas para calcular distribuciones uniformes, normales(la de gauss), 
#Logaritmicas normales y tambien de exponenciales negativas y por supuesto de las funciones gamma y beta. (Esto fuera de la programacion es interesante asi que podrias repasarlo
#En los libros de calculo y calculo avanzado)
#Ahora si vengan los ejemplos 
import random

#Para obtener un elemento aleatorio entre 0 y 1 
numero_aleatorio = random.random()
print(numero_aleatorio)

#Ahora para obtener un random dentro de un rango especifico y lo que obtendremos sera un tipo flotante 
r = random.uniform(1, 50)
print(r)
print(type(r))

#Ahora lo trataremos con los numeros enteros 
r = random.randint(1,50)
print(r)
print(type(r))

#En el antarior caso se toma en cuenta el limite superior pero si lo queremos excluir entonces sera asi
r =  random.randrange(1,50)
print(r)
print(type(r))

#Ahora como obtenemos un random de una distribucion normal para este caso nesesitaremos una media y una desviacion estandar y atmbien tenemos un tipo flotante 
r =  random.normalvariate(50, 3.6)
print(r)
print(type(r))
#Esto se puede llevar a cabo con las distribuciones mencionadas arriba pasando los parametros correctos

#Tambien podemos utilizar secuencias para obtener elementos aleatorios de ellas 
lista = "abc1234j1872nqin98"
r =  random.choice(lista)
print(r)
print(type(r))

#Para que retorne mas de un elemento y seleccionemos cuantos va a regresar sin repetir elementos 
r = random.sample(lista,3)
print(r)
print(type(r))

#Ahora repitiendo elementos 
r = random.choices(lista, k = 5)
print(r)
print(type(r))

#Otro ejemplo
lista1 = list("abcnfiqhnqpodfhnpqhpfiob")
random.shuffle(lista1)
print(lista1)

#En realidad todos los ejemplos pasados no son en realidad numeros aleatorios reales como dije en el principio ya que son numeros pseudoaleatorios ya que 
#Detras de la eleccion de estos numeros podemos encontrar algoritmos que los generan de la manera mas parecia a lo que seria una distribucion aleatoria 
#Y por tanto podemos replicar dichos numeros 

random.seed(10)
r = random.random()
print(r)

random.seed(40)
r = random.random()
print(r)

random.seed(10)
r = random.random()
print(r)

#Y como observamos alterando las tablas de distribucion del algoritmo de random con seed podemos obtener el mismo resultado 

#Otra de las aplicaciones de los numeros alaeatorios es en diferentes aspectos de la seguridad como por ejemplo la generacion de contraseñas 
#Los patrones de cifrado, generacion de tokens, en jwt o directamente en claves de acceso de servidores y sus aplicaciones escalan de acuerdo a la aplicacion en desarrrollo 
#Por tanto aveces nesesitamos de lo que se llaman numeros aleatorios criptograficamente fuertes y en este caso es algo que random solamnete nos puede proveeer de manera 
#Muy basica y para su mejor uso tenemos el modulo de secrets
import secrets

#Numero aleatorio sin tomar el limite superior
r = secrets.randbelow(100)
print(r)
print(type(r))

#Para obtener un entero de n bits aleatorios 
r = secrets.randbits(32)
print(r)
print(type(r))

#Para seleccionar un elemento de una secuencia 
secrets.choice(lista)
print(r)
print(type(r))

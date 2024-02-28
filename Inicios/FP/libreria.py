#Ahora veamos uans libreria de python que nos permite tener estrucutar de datos no mutables, esta libreria es pyrsistent

#Ejemplo de actualizar el ultimo elemento de la lista sin mutar la original 
def actualizar(lista, valor):
    lista1 = lista[:]
    lista1[-1] = valor
    return lista1

milista = [1,2,3,4,5]
nl = actualizar(milista, 6)
print(milista)
print(nl)

#Ahora veremos como seria con pyrssitent, nessitaras instalar esta biblioteca con el comando pip install pyrsistent 
from pyrsistent import pvector, v, pmap, m, pset, s, freeze, thaw, PClass, field

#La primer estructura de datos a revisar sera el pvector, que seria similar a la lista pero dentro de las estructuras no mutables y a v que sera de ayuda a crear los vectores
#Declaramos la lista y la transformamos a pvector 
vec = pvector([1,2,3])

#Tambien podriamos hacerlo solamente con v, esta itera a travez de los parametros de la lista creando un pvector
vec2 = v(1,2,3)

#Y el manejo de los pevector son bastante parecidos a la lista:
print(vec[1])
print(vec2[0])

#A la hora de mutar, la original no se modifica por lo que nos simplifica el trabajo a la hora de la creacion de nuevas listas sin que queremos mutaciones de las listas
#´Para poder ver su retorno de esto sera dentro de una funcion 
def nuevopvector():
    nvpvector = vec.append(6)
    print(nvpvector)
    return nvpvector
nuevopvector()
print(vec)

#Mas sin embargo no podemos utilizar el indexado para colocar un valor, para eso utilizamos set
def nuevopvector2():
    nvpvector2 = vec.set(0, 25)
    print(nvpvector2)
    return nvpvector2
nuevopvector2()
print(vec)

#Y ahora el equivalente al diccionario, este me parece muy interesante ya que suele ser muy util 
#Creamos el pmap
d1 = pmap({1:"Hola", 2:"Mundo", 3:"Zy"})
print(d1)

#Lo podemos hacer con la funcion m 
d2 = m(a = 1, b= 2, c =3)
print(d2)

#La busqueda por indice se mantienen de la manera normal
print(d1[3])
print(d2["a"])

#Para modificar al igual que en la lista debemos utilizar set
r = d2.set('hola', 'mundo')
print(d2)
print(r)

#Ahora para trabajar con sets
s1 = pset(['manzana',' guayaba'])
print(s1)

s2 = s('sandia', 'limon')
print(s2)

#Y ahora veremos las opreaciones comunes con los sets
s3 = s1 | s2
print(s3)

#Podemos adicionar
s4 = s1.add('platano')
print(s4)

#Y eliminar
s5 = s1.remove('manzana')
print(s5)

#Y ahora para las colecciones anidadas por ejemplo una tupla o simplemente listas con diferentes tipos de estructuras de datos dentro de dicha lista
datos = [[1,2,3], [3,4,5], {"a":10, "b": 10}]
print(datos)

#Como podremos ver con esto, freeze vulven inmutable con su diferente tipo a cada una de las estructuras de la lista
d1 = freeze(datos)
print(d1)

#Y podemos regresar a la estructura original 
r = thaw(d1)
print(r)

#Y por ultimo crear clases con objetos inmutables 
#Primero tenemos que hacer una herencia a Pclass
class Ejemplo(PClass):
    #Los atributos los colocamos como field 
    x = field()
    y = field()
    
    def translation(self, dx, dy):
        return self.set(x = self.x + dx, y = self.y + dy)

punto1 = Ejemplo(x = 1, y = 2)
punto2 = punto1.translation(5,5)

print(punto1)
print(punto2)

#No podemos colocar nuevos atributos solamente podemos utilizar los que han sido declarados explcitamente en la clase
try: punto1.w = 5
except Exception as e: print(e)
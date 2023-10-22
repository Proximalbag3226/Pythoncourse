#Los scopes son los valores de las variables a los cuales la funcion declarada puede acceder y a los que son inaccesible para ella

nombre = "Luis"

def saludo_nombre():
    print(f"Hola {nombre}")

saludo_nombre()

#Esta variable es de scopes global ya que es accesible para todas las funciones declaradas en todo el programa 
#Por ejemplo tenemos tambien la variable de forma local

def saludo_nombre2():
    local = "Fer"
    print(f"Hola {nombre}")
    print(f"La variable de forma local es {local}")

print(f"La variable global es {nombre}")
saludo_nombre2()
#Si  trataramos de imprimir la variable local desde otra parte que no es la funcion del codigo esto nos va a desplegar un error que nos dira que la variable no este definida

#Tambien podemos tener variables locales anidadas dentro de otras por ejemplo

def nombre_edad():
    nombre = "Luis"
    edad = 17
    print(f"Hola tu nombre es {nombre}")
    def edad1():
        edad = 19
        print(f"Y tu edad es de {edad}")
    edad1()

nombre_edad()

#como podemos obvservar la variable de edad esta de un color mas oscura ya que no esta siendo usada porque la variable local anidada esta ocupando su trbajo 
#podemos utilizar la palabra reservada nonlocal para poder acceder a una variable local de mayor "rango"

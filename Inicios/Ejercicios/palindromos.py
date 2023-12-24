#Se da un numero y se pide evaluar si en numero en cuestion es palindromo, que sea igual leido de derecha a izquierda y viceversa

#Pedimos un numero para evaluar
numero = input("Ingrese el numero a evaluar ").strip()

#Definimos una funcion que pueda relizar esta accion
def Palindromo(string):
    reversed = string[::-1]
    if string == reversed:
        print("El numero es igual")
    else:
        print("No  es igual")
        
Palindromo(numero)

#Este es el metodo mas facil aunque tambien se puede realizar por medio de ciclos for

#Definimos la funcion
def es_palindromo(string):
    
    #La longitud del string
    longitud = len(string)
    
    #El ciclo for para evaluar la palabra, donde solamente evaluamos hasta la mitad ya que no ocupamos evaluar completo 
    for i in range(longitud // 2):
        
        #Evaluamos la condicion
        if string[i] != string[longitud - 1 - i]:
            return False
    
    return True

# Imprimimos los resultados
numero2 = input("Ingrese un numero  para evaluar: ")
if es_palindromo(numero2):
    print(f"{numero2} es igual")
else:
    print(f"{numero2} no es igual")
    
#Estos mismos codigos se pueden utilizar para la evaluacion de palabras, solamente abria que cambiar un poco
#Ejemplo
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para hacer la comparación sin distinción de mayúsculas y minúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco para considerar frases palindrómicas
    
    # Verificar si la palabra es igual a su inversa
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Imprimimos resultados
palabra = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")



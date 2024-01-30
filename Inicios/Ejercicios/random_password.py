#Se pide crear un programa para crear una contraseña con combinaciones aleatorias hasta de 20 caracteres
import random
import string

longitud = int(input("Ingrese la longitud en numeros de la contraseña: ").strip())

def random_password():
    try:
        if longitud < 20:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))
            print(f"La contraseña generada es: {password}")
        else:
            print("La longitud es demasiado grande")
    except ValueError:
        print("Ingrese un numero entero")
random_password()
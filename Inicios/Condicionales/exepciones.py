#Para el manejo de exepciones que pueden ser errores o casos que no tenemos contemplados que sucesan dentro del programa se pueden utilizar los condicionales
#U otros bloques de codigo para el manejo de estos casos exepcionales que se pueden llegar a presentar

#Tenemos los ya conocidos if que hemos visto 

def dividir(num1, num2):
    if num2 == 0:
        print("No es posible dividir entre 0")
    else:
        return num1 / num2

dividir(5,0)

#Tambien podemos manejar las exepciones con los bloques de codigo try y except, en este caso try es la parte del codigo que es "Lo que esperamos correcto"
#En caso de que el try no se cumpla correctamente los except con sus respectivos errores saltaran a relusir en el codigo interriumpiendo su ejecucion y saltando 
#La alerta que les hayamos indicado

#Ejemplo
try:
    # Código que puede generar una excepción
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

#Value error hace referencia a un error con el valor de alguno de los datos, ejemplo si pasamos un int en vez de un float
except ValueError:
    # Se ejecuta si ocurre una excepción de tipo ValueError
    print("Error: Ingrese un número válido.")

#Aqui una clasica que es el error al divir entre 0
except ZeroDivisionError:
    # Se ejecuta si ocurre una excepción de tipo ZeroDivisionError
    print("Error: No se puede dividir por cero.")

else:
    # Se ejecuta si no ocurre ninguna excepción en el bloque try
    print("Operación realizada con éxito.")

#Por ultimo la secuencia finallly siempre sera ejecutada al final del codigo no importa que 
finally:
    # Se ejecuta siempre, independientemente de si hay excepciones o no
    print("Este bloque siempre se ejecuta.")


#Aqui otro ejemplo
try:
    # Código que puede generar una excepción
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

#La palabra reservada "as" la podemos utilizar para poder obtener mas informacion acerca del error 
except (ValueError, ZeroDivisionError) as e:
    # Maneja excepciones de tipo ValueError o ZeroDivisionError
    print(f"Error: {e}")

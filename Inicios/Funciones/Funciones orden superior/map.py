#Las funciones de orden superior son funciones que pueden resivir como argumento alguna otra funcion, estas funciones pueden retornar funciones o listas
#La funcion map es una de las utilizadas y sirve para transformar varios elementos de un iterable, aplica la funcion argumento a cada elemento del iterable
#Ejemplo, vamos a transformar los elementos de la siguiente lista a 

#Declaramos una lista con los nombres
nombres = ['luis','juan','fernanda']
#Creamos una variable que contenga la funcion map y la funcion upper que sirve para pasar a mayusuculas, tenemos que transformar la lista de nombres a string para poder
#Utilizar upper y despues el resultado de utilizar map lo transformamos en list para que sea un resultado deseado
lista_mayusculas = list(map(str.upper,nombres))
#Por ultimo imprimimos el resultado 
print(lista_mayusculas) 
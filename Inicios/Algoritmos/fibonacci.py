#Aqui tenemos la serie de fibonacci en pytho, que tambien puede ser interpretada como un algoritmo para series

#Definimos la funcion para crear la serie
def fib(n):
    
    #Establecemos una condicion de ejecucion para saber que valor devolver en caso de que n<2
    if n < 2:
        return n
    else:
        #La serie de fibonacci esta definida por la siguiente exprecion fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

#Imprimimos los resultados
print(fib(8))               

#Y ahora la serie hasta su 10mo termino
for i in range(10):
    print(fib(i))
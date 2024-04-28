#Esto como tal no es un algoritmo pero se me ocurrio ponerlo aqui porque pues puede tener utilidad para ciertas situaciones en donde se requeiere la aplicacion 
#Del calculo integral, aunque no es tan avanzado y es un ejemplo simple pero podria adaptarse para las nesesidades de cada aplicacion

#Bueno entendemos nosotros por integral asi en un lenguaje vago y no tan tecnico, el area bajo la curva de una funcion f(x) y como calculamos esa area
#Bueno una integral tambien se puede expresar con sumatorias y estas mismas integrales se pueden resolver con sumas de riemman que es practicamente lo mismo
#Recordemos el segundo teorema fundamental del calculo que dice que sea una funcion f(x) continua en a,b y sea F(x) cualquier primitiva o antiderivada
#de f(x) en a,b entonces la integral definida de f(X) en ese intervalo se puede expresar en terminos de la primitiva como F(b) - F(a)
#Y en una forma mas sencilla de tomar esto es calculando esta area dividiendola en rectangulos y sumando el area de ellos, pero si estos rectangulos son muy 
#Grandes tenemos que el error que vamos a tener en los calculos del area bajo la curva sera mas significativos por lo tanto debemos minimizar esta area de 
#Dichos rectangulos para asi poder tener estimaciones mas precisas, recordemos que el are de dicho rectangulo es de Δx y la altura seria f(x)
#Y para obtener Δx debemos realizar la siguiente operacion que consiste en restar los limites de integracion y dividirlos entre la cantidad de Δx
#Δx = (b-a)/n y la sumatorio para calcular el area bajo la curva seria desde i = n hasa lim cuando n -> ∞ de f(xi) * Δx
#Como podemos pasar esto a codigo, muy facil ya que podemos interpretar la sumatoria como un ciclo for de acciones repetidas

#Mucho texto y vamos con el codigo 

def funcion(x):
    
    #Definimos una funcion para integrar que para ejemplo usaremos x^2
    return x ** 2

#Para la funcion de integral definida tomaremos como argumentos los limites de integracion y la n cantidad de rectangulos
def integral_definida(limite1, limite2, n):
    
    #Usamos la formula para calcular el valor de Δx
    dx = (limite2 - limite1 )/n
    
    #Iniciamos el valor de la sumatoria en 0 
    x = limite1
    suma = 0
    
    #Realizamos la sumatoria hasta el n valor
    for i in range(n):
        
        #Aqui relizamos la sumatoria de f(x) * Δx 
        suma += funcion(x) * dx
        
        #Y asignamos el valor para la siguiente iteracion de f(xi)
        x += dx
        
    #Retornamos el valor total     
    return suma

#Y el ejemplo calcularemos el area bajo la curva de la funcion f(x) = x^2 de 3 hasta 8
resultado = integral_definida(3, 8, 3000)
print(f"El resultado de la integral es de: {resultado}")

#Claro que ha mayores iteraciones de n el resultado tendra menos margen de error

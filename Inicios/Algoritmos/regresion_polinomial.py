#En el algoritmo de regresion lineal nos puede servir para casos donde tenemos datos que siguen una tendencia lineal para cada uno de ellos sin tener tantas variaciones
#Es util para las diferentes situaciones que podemos encontrar aveces dentro de la realizacion de predicciones o implementaciones en modelos de aprendizaje automatico 
#Pero y si los datos que tenemos no siguen esta tendencia lineal y en vez de eso siguen algun tipo de grafica que se azemeja a la de una ecuacion polinomial
#Para este caso tenemos esta variante la regresion polinomial, para empezar pues un polinomio es la suma o resta de n terminos algebraicos que se componen de 
#Un coeficiente dentro de los numeros reales (para este caso) y una o mas variables elevadas a coeficientes no negativos ejemplo: 6x^3 + x^2 + 8x donde x es la variable 
#Independiente, 6,1 y 8 son los coeficientes y 3,2,1 son los exponentes, para la regresion polinomial se puede ver de esta manera: y = θ0 +  θ1x1 + θ2x1^2 que es de grado 2 
#Donde y es la variable dependeiente a predecir θ son los coeficientes de las variables independientes x1
#Para hacer mas interesnate eso tenemos que la regresion polinomial no es directamente con la formula anterior si no que mas bien podemos tenemer polinomios de grado n 
#Hasta adaptarnos a nuestros datos de manera que el ECM (error cuadratico medio) se el menor posible para tener fe en nuestro modelo que entregue los resultados correctos 

#Ahora vamos con el ejemplo 

#Importamos las librerias 
import numpy as np
import matplotlib.pyplot as plt

#Generamos los datos aleatorios para el modelo que en este caso sera de produccion de dulces por año 
np.random.seed(0)

#Años de producción de 2000 a 2020
años = np.arange(2000, 2025)

#Simulamos una funcion cuadratica aunque puede veriarse para otros casos el tipo de funcion a generar 
cantidad_dulces = 1.2 * (años - 2010) ** 2 + 4500

#Añadimos ruido para hacerlo mas relizta pero no tanto 
cantidad_dulces += np.random.normal(loc=0, scale=15, size=len(años))  

#Asegurarse de que los valores no sean negativos y separar cada valor con una coma 
cantidad_dulces = np.maximum(cantidad_dulces, 0)
print(cantidad_dulces)
print(type(cantidad_dulces))

#Ahora vamos a pasar estos datos a una forma de array de numpy cada año tendra su variable de produccion
x = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
y = cantidad_dulces

#Vamos a declarar el año que queremos predecir 
año_prediccion = 2025

#Y con la funcion de polyfit vamos a encontrar lo coeficientes para la ecuacion cuadratica (exponente 2)
#coeficiente = np.polyfit(x,y,2)

#A polyval le pasamos esos coeficientes encontrados y el año de la prediccion
#a = np.polyval(coeficiente, año_prediccion)

#print(f"Para el año {año_prediccion} la prediccion es {a}")

#Todo lo anterior nos puede servir claro que si pero tambien podemos mejorarlo ya que no nos vamos a conformar con solo comprobar con el exponente 2 para esta funcion 
#Dado que podemos tener valores mas exactos provando diferentes exponentes para nuestra prediccion para ver cual nos arroja un menor ECM

#Creamos un dataset para las funciones polinomiales que vamos a guardar
polinomios = []

#Y lo haremos con un ciclo for 
for i in range(0,10):
    
    #Econtramos los coeficientes para las ecuaciones polinomiales
    coeficiente = np.polyfit(x,y,i)
    
    #Ajustamos los polinomios con grado i 
    polinomio = np.poly1d(coeficiente)
    
    #Y lo guardamos 
    polinomios.append(polinomio)
    
    #Creamos la prediccion con base en los coeficientes y el año 
    prediccion = np.polyval(coeficiente, año_prediccion)
    print(f"Para el año {año_prediccion} con el grado{i} la prediccion es {prediccion}")
    
    #Graficamos el polinomio para la prediccion
    plt.plot(x, polinomio(x), label=f'Grado {i}')
    
#Ahora nos preguntaremos como podemos elegir el dato correcto que nos permita tener la prediccion mas cercana a la relidad y para esto vamos a calcular el ECM para 
#Cada uno de los grados polinomiales
    
#Graficamos los datos reales
plt.scatter(x, y, color='red', label='Datos reales')

#Configuraciones adicionales del gráfico
plt.title('Dulces producidos vs Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Dulces')
plt.grid(True)
plt.legend()
plt.show()

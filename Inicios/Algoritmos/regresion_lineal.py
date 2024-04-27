#Que es la regresion lineal? bueno es un algoritmo basico del machine learning basado en una tecnica estadistica del mismo nombre
#Esta consiste en compreder la relacion que hay entre las variables dependientes y las independientes. Como su nombre lo indica este
#Algforitmo busca encontrar una relacion linal entre ambas variables lo que consiste en ajustar una linea recta a los datos que represente
#Mejor la realcion entra ambos datos, este modelo esta representado con la forma matematica de y = la sumatoria de 0 hasta n de BnXn + ε 
#Donde y es la variable dependiente que vamsoa calcular, las Xn son las variables dependientes y Bn son los coeficientes de la pendiente de 
#La relacion entre cada y para cada x respectivamente y ε es el error medio entre el valor obvservado y el valor predicho por el modelo el cual 
#Se busca encontrar los valores de los coeficientes Bn que minimcen el cuadrado de errores para encontrar valores mas cercanos a los esperados cada vez
#Esto se aplica al ML donde tenemos un conjunto de datos para entrenar a este algoritmo para que posteriormente pueda realizar alguna prediccion de los 
#Valores futuros para dic ho conjunto de datos y ademas de existir la forma mas basica que seria esta podemos encontrarnos tambien con algunas de sus
#Variantes como pueden ser la regresion multiple, la regresion polinomica etc.
#El entrenamiento de este modelo se basa en el punto anteriormente mencionado que consiste en el echo de encontrar valores para Bn que minimicen el rango de error
#Y nesesitamos aplicar alguna formula matemaica para conocer estas incognitas usando en este caso la ecucacion normal que seria: B = (X^TX)^-1 * X^TY
#Para usarla correctamente nesesitamos pasar la tabla de valores de los que disponemos a vectores y sustiturir dichos vectores en la formula 

#Pero en fin es la teoria base para la regresion lineal, ahora vamos a ver como podemos pasarlo a un codigo muy simple y sencillo 

#Importamos la dependencias que vamos a usar (algunas de ellas las nessitaras instalar con pip install)
import matplotlib.pyplot as plt
import numpy as np

#Declaramos los vectores de una tabla de valores 

#Donde "x" es la altura 
x = [173, 171, 189, 181]

#Y "y" el peso
y = [81, 72, 96, 94]

#Agregamos el termino "bias" para "mover" la linea de la regresion lineal de ariba a abajo 
#Lo que hace esta linea de codigo es generarnos una matriz de 2 x 4 que contiene nuestro termino bias y los datos de la altura 
x_1 = np.c_[np.ones(4), x]
print(x_1)

#Aplicamos la ecuacion normal pero ahora sustituimos los vectores que ya hemos creado usando numpy 

#Aqui aplicamos una simple obtencion de la inversa de dicha matriz y traducimos la ecucion normal a un lenguaje de numpy 
B = np.linalg.inv(x_1.T.dot(x_1)).dot(x_1.T).dot(y)

#Y ahora tenemos los valores de B
print(B)

#Grafiquemos los puntos
plt.scatter(x,y, s=40, c='#06d6a0')

#Graficamos la linea 
limites_x = [170, 190]
lmites_x1 = np.c_[np.ones(2), limites_x]
limites_y = lmites_x1.dot(B)
plt.plot(limites_x, limites_y, 'r-')

#Y configuramos el grafico para mostar los datos nesesarios 
plt.axis([170, 190, 70, 100])
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.title("Altura y prediccion de peso")
plt.grid()

#Y mostramos el grafico
plt.show()

#Bien ahora que tenemos el modelo y el grafico para representarlo, podemos realizar una prediccion de esta manera 
peso_zy = B[0] + (B[1] * 179)
print(f"El peso de zy es de: {peso_zy}")


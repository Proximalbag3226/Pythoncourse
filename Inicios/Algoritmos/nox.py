import numpy as np
import matplotlib.pyplot as plt

# Generamos los datos aleatorios para el modelo que en este caso sera de produccion de dulces por año 
np.random.seed(0)

# Años de producción de 2000 a 2024
años = np.arange(2000, 2025)

# Simulamos una función cuadrática para la cantidad de dulces producidos cada año
cantidad_dulces = 1.2 * (años - 2010) ** 2 + 4500

# Añadimos un poco de ruido para hacerlo más realista
cantidad_dulces += np.random.normal(loc=0, scale=50, size=len(años))

# Asegurarse de que los valores no sean negativos
cantidad_dulces = np.maximum(cantidad_dulces, 0)

# Declaramos el año que queremos predecir 
año_prediccion = 2025

# Creamos arrays de NumPy con esos datos
x = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
y = cantidad_dulces

# Inicializamos una lista para almacenar las funciones polinomiales
polinomios = []

# Iteramos sobre diferentes grados de polinomios
for i in range(0, 11):
    # Ajustamos un polinomio de grado i a los datos
    coeficientes = np.polyfit(x, y, i)
    polinomio = np.poly1d(coeficientes)
    
    # Guardamos el polinomio en la lista
    polinomios.append(polinomio)

    # Predicción para el año especificado
    prediccion = np.polyval(coeficientes, año_prediccion)
    print(f"Para el año {año_prediccion} con el grado {i}, la prediccion es {prediccion}")

    # Graficamos el polinomio ajustado
    plt.plot(x, polinomio(x), label=f'Grado {i}')

# Graficamos los datos reales
plt.scatter(x, y, color='red', label='Datos reales')

# Configuraciones adicionales del gráfico
plt.title('Dulces producidos vs Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Dulces')
plt.grid(True)
plt.legend()
plt.show()

#Importamos las librerias 
import numpy as np
import matplotlib.pyplot as plt

#Generamos datos de ejemplo
np.random.seed(0)
x = np.linspace(0, 10, 50)
y = 2.5 * x + np.random.normal(0, 1, 50)

#Definimos el rango de valores para la variable independiente
xp = np.linspace(-1, 1, 10000) * 2 * np.pi

#Creamo subgráficos para mostrar los resultados
fig, ax = plt.subplots(3, 3, figsize=(15, 15))

for n in range(3):
    for k in range(3):

        order = 2 * n + 2 * k + 1
        print(order)
        z = np.polyfit(x, y, order)
        p = np.poly1d(z)

        ax[n, k].scatter(x, y, label="Datos reales", s=10)
        ax[n, k].plot(xp, p(xp), label="Polinomio de orden {}".format(order), color='C1')
        ax[n, k].legend()

plt.tight_layout()
plt.show()

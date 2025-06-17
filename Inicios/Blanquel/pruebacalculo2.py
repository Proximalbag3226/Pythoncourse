import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import time
import pandas as pd

x = sp.symbols('x')

# Construir polinomio de Maclaurin
def construir_maclaurin(f, x, n):
    Pn = 0
    for i in range(n + 1):
        derivada = f.diff(x, i)
        derivada_en_0 = derivada.subs(x, 0)
        termino = (derivada_en_0 / math.factorial(i)) * x**i
        Pn += termino
    return Pn

# Función principal para ejecutar cálculo
def ejecutar():
    entrada_funcion = entry_funcion.get()
    try:
        f = sp.sympify(entrada_funcion)
        f_lambd = sp.lambdify(x, f, 'numpy')
    except:
        messagebox.showerror("Error", "Función inválida.")
        return

    try:
        valor_x = float(entry_valor_x.get())
    except:
        messagebox.showerror("Error", "x debe ser un número.")
        return

    modo = var_modo.get()
    t0 = time.time()
    valor_real = f_lambd(valor_x)

    if modo == "n":
        try:
            n = int(entry_n.get())
        except:
            messagebox.showerror("Error", "n debe ser entero.")
            return
        Pn = construir_maclaurin(f, x, n)
    else:
        try:
            epsilon = float(entry_epsilon.get())
        except:
            messagebox.showerror("Error", "ε debe ser un número.")
            return
        n = 0
        while True:
            Pn = construir_maclaurin(f, x, n)
            Pn_lambd = sp.lambdify(x, Pn, 'numpy')
            valor_aprox = Pn_lambd(valor_x)
            error = abs(valor_real - valor_aprox)
            if error < epsilon:
                break
            n += 1

    Pn_lambd = sp.lambdify(x, Pn, 'numpy')
    valor_aprox = Pn_lambd(valor_x)
    error = abs(valor_real - valor_aprox)
    t1 = time.time()
    tiempo = t1 - t0

    # Mostrar resultados
    salida_resultados.config(state="normal")
    salida_resultados.delete(1.0, tk.END)
    salida_resultados.insert(tk.END, f"Polinomio P{n}(x):\n{Pn}\n\n")
    salida_resultados.insert(tk.END, f"f({valor_x}) = {valor_real}\n")
    salida_resultados.insert(tk.END, f"P{n}({valor_x}) = {valor_aprox}\n")
    salida_resultados.insert(tk.END, f"Error absoluto = {error}\n")
    salida_resultados.insert(tk.END, f"Orden n = {n}\n")
    salida_resultados.insert(tk.END, f"Tiempo de ejecución: {tiempo:.6f} s\n")
    salida_resultados.config(state="disabled")

    # Tabla
    df = pd.DataFrame({
        'Descripción': ['Valor exacto', f'P{n}({valor_x})', 'Error', 'Orden n', 'Tiempo (s)'],
        'Resultado': [valor_real, valor_aprox, error, n, tiempo]
    })
    salida_tabla.config(state="normal")
    salida_tabla.delete(1.0, tk.END)
    salida_tabla.insert(tk.END, df.to_string(index=False))
    salida_tabla.config(state="disabled")

    # Gráfica
    ax.clear()
    x_vals = np.linspace(valor_x - 2, valor_x + 2, 400)
    y_real = f_lambd(x_vals)

    # Corrección si Pn devuelve escalar
    try:
        y_aprox = Pn_lambd(x_vals)
    except:
        y_aprox = np.full_like(x_vals, Pn_lambd(0))

    ax.plot(x_vals, y_real, label="f(x)", color="blue")
    ax.plot(x_vals, y_aprox, "--", label=f"P{n}(x)", color="red")
    ax.set_title("Comparación gráfica")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)
    canvas.draw()

# Crear GUI
root = tk.Tk()
root.title("Calculadora de Polinomios de Maclaurin")

# Entradas
tk.Label(root, text="Función f(x):").grid(row=0, column=0, sticky="w")
entry_funcion = tk.Entry(root, width=40)
entry_funcion.grid(row=1, column=1, columnspan=3)

tk.Label(root, text="Valor de x:").grid(row=1, column=0, sticky="w")
entry_valor_x = tk.Entry(root)
entry_valor_x.grid(row=1, column=1)

# Modo de cálculo
var_modo = tk.StringVar(value="n")
tk.Radiobutton(root, text="Usar n fijo", variable=var_modo, value="n").grid(row=2, column=0, sticky="w")
entry_n = tk.Entry(root)
entry_n.grid(row=2, column=1)

tk.Radiobutton(root, text="Buscar n por ε", variable=var_modo, value="epsilon").grid(row=3, column=0, sticky="w")
entry_epsilon = tk.Entry(root)
entry_epsilon.grid(row=3, column=1)

# Botón de cálculo
tk.Button(root, text="Calcular", command=ejecutar, bg="green", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

# Resultados
tk.Label(root, text="Resultados:").grid(row=5, column=0, sticky="w")
salida_resultados = tk.Text(root, height=8, width=70, state="disabled", bg="#f0f0f0")
salida_resultados.grid(row=6, column=0, columnspan=4)

# Tabla
tk.Label(root, text="Tabla resumen:").grid(row=7, column=0, sticky="w")
salida_tabla = tk.Text(root, height=5, width=70, state="disabled", bg="#f0f0f0")
salida_tabla.grid(row=8, column=0, columnspan=4)

# Gráfica
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=9, column=0, columnspan=4)

root.mainloop()

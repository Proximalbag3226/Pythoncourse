import sys
import math
import time
import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QRadioButton,
    QMessageBox, QButtonGroup, QFrame 
)
from PySide6.QtCore import Qt

x = sp.symbols('x')

app_style_sheet = """
QMainWindow {
    background-color: #f0f2f5;
    color: #333333;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 14px;
}

QLabel {
    color: #555555;
    padding: 5px 0px;
}

QLineEdit {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    border-radius: 5px;
    padding: 8px 10px;
    selection-background-color: #007bff;
    selection-color: white;
}

QLineEdit:focus {
    border: 1px solid #007bff;
    background-color: #f7faff;
}

QPushButton {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
    min-width: 100px;
}

QPushButton:hover {
    background-color: #0056b3;
}

QPushButton:pressed {
    background-color: #004085;
}

QRadioButton {
    spacing: 5px;
    padding: 5px 0px;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
    border-radius: 8px;
    border: 1px solid #cccccc;
    background-color: #ffffff;
}

QRadioButton::indicator:checked {
    background-color: #007bff;
    border: 1px solid #007bff;
}

QTextEdit {
    background-color: #ffffff;
    border: 1px solid #dddddd; 
    border-radius: 5px;
    padding: 10px;
    color: #333333;
    font-family: 'Consolas', 'Courier New', monospace;
}

QFrame#InputFrame { 
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
}

QToolBar {
    background-color: #e9ecef;
    border: none;
    padding: 5px;
    border-radius: 5px;
}
QToolButton {
    background-color: transparent;
    border: none;
    padding: 5px;
}
QToolButton:hover {
    background-color: #d0d0d0;
    border-radius: 3px;
}

QScrollBar:vertical {
    border: none;
    background: #f0f0f0;
    width: 12px;
    margin: 15px 0 15px 0;
    border-radius: 0px;
}
QScrollBar::handle:vertical {
    background: #cccccc;
    min-height: 20px;
    border-radius: 5px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
QScrollBar:horizontal {
    border: none;
    background: #f0f0f0;
    height: 12px;
    margin: 0 15px 0 15px;
    border-radius: 0px;
}
QScrollBar::handle:horizontal {
    background: #cccccc;
    min-width: 20px;
    border-radius: 5px;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
"""

def construir_maclaurin(f, x_sym, n):
    Pn = 0
    for i in range(n + 1):
        derivada = f.diff(x_sym, i)
        derivada_en_0 = derivada.subs(x_sym, 0)
        termino = (derivada_en_0 / math.factorial(i)) * x_sym**i
        Pn += termino
    return Pn

class MaclaurinApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Polinomios de Maclaurin")
        self.setGeometry(100, 100, 900, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self._init_ui()

    def _init_ui(self):
        input_frame = QFrame()
        input_frame.setObjectName("InputFrame")
        input_layout = QGridLayout(input_frame)

        input_layout.addWidget(QLabel("Función f(x):"), 0, 0)
        self.entry_funcion = QLineEdit("sin(x)")
        input_layout.addWidget(self.entry_funcion, 0, 1, 1, 2)

        input_layout.addWidget(QLabel("Valor de x:"), 1, 0)
        self.entry_valor_x = QLineEdit("0.5")
        input_layout.addWidget(self.entry_valor_x, 1, 1)

        self.radio_n = QRadioButton("Usar n fijo")
        self.radio_n.setChecked(True) 
        self.entry_n = QLineEdit("5")
        
        self.radio_epsilon = QRadioButton("Buscar n por ε")
        self.entry_epsilon = QLineEdit("0.001")

        mode_group = QButtonGroup(self)
        mode_group.addButton(self.radio_n)
        mode_group.addButton(self.radio_epsilon)

        input_layout.addWidget(self.radio_n, 2, 0)
        input_layout.addWidget(self.entry_n, 2, 1)
        input_layout.addWidget(self.radio_epsilon, 3, 0)
        input_layout.addWidget(self.entry_epsilon, 3, 1)

        self.radio_n.toggled.connect(lambda: self.entry_n.setEnabled(self.radio_n.isChecked()))
        self.radio_n.toggled.connect(lambda: self.entry_epsilon.setEnabled(self.radio_epsilon.isChecked()))
        self.entry_n.setEnabled(self.radio_n.isChecked())
        self.entry_epsilon.setEnabled(self.radio_epsilon.isChecked())

        self.btn_calcular = QPushButton("Calcular")
        self.btn_calcular.clicked.connect(self.ejecutar)
        
        input_layout.addWidget(self.btn_calcular, 4, 0, 1, 3, alignment=Qt.AlignCenter)

        self.main_layout.addWidget(input_frame)

        self.main_layout.addWidget(QLabel("Resultados:"))
        self.salida_resultados = QTextEdit()
        self.salida_resultados.setReadOnly(True)
        self.main_layout.addWidget(self.salida_resultados)


        self.main_layout.addWidget(QLabel("Tabla resumen:"))
        self.salida_tabla = QTextEdit()
        self.salida_tabla.setReadOnly(True)
        self.main_layout.addWidget(self.salida_tabla)

        graph_layout = QHBoxLayout()

        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasQTAgg(self.fig)
        
        self.toolbar = NavigationToolbar2QT(self.canvas, self)


        self.main_layout.addWidget(self.toolbar)
        self.main_layout.addWidget(self.canvas)


    def mostrar_error(self, mensaje):
        QMessageBox.critical(self, "Error", mensaje)


    def ejecutar(self):

        self.salida_resultados.clear()
        self.salida_tabla.clear()
        self.ax.clear()
        self.canvas.draw()

        f_str = self.entry_funcion.text().strip()
        try:
            f = parse_expr(f_str, evaluate=True)
            f_lambd = sp.lambdify(x, f, 'numpy')
        except Exception as e:
            self.mostrar_error(f"Funcion inválida: {e} asegúrate de usar la varialbe x en tu expresion")
            return

        try:
            valor_x = float(self.entry_valor_x.text().strip())
        except ValueError:
            self.mostrar_error("El valor de x debe ser un numeros")
            return

        try:
            valor_real = f_lambd(valor_x)
            if not math.isfinite(valor_real):
                self.mostrar_error(f"La funcion f(x) no es finita en x={valor_x} valor obtenido: {valor_real}")
                return
        except Exception as e:
            self.mostrar_error(f"Error al evaluar f(x) en x={valor_x}: {e} revisa tu funcion o el valor de x")
            return

        Pn = 0
        n = 0
        t0 = time.time()

        if self.radio_n.isChecked():
            try:
                n = int(self.entry_n.text().strip())
                if n < 0:
                    raise ValueError("n debe ser un entero no negativo")
            except ValueError as e:
                self.mostrar_error(f"El valor de n debe ser un numero entero no negativo: {e}")
                return
            
            Pn = construir_maclaurin(f, x, n)
        else: 
            try:
                epsilon = float(self.entry_epsilon.text().strip())
                if not (0 < epsilon < 1):
                    raise ValueError("ε debe ser un nmero positivo")
            except ValueError as e:
                self.mostrar_error(f"ε debe ser un número positivo: {e}")
                return
            
            Pn_actual = sp.sympify(0)
            
            while True:
                derivada = f.diff(x, n)
                derivada_0 = derivada.subs(x, 0)
                
                try:
                    termino_n = (derivada_0 / math.factorial(n)) * x**n
                except (ZeroDivisionError, AttributeError, TypeError):
                    termino_n = sp.sympify(0)
                    
                Pn_actual += termino_n
                
                try:
                    Pn_lambd_iter = sp.lambdify(x, Pn_actual, 'numpy')
                    valor_aprox = Pn_lambd_iter(valor_x)
                    if not math.isfinite(valor_aprox):
                        raise ValueError("El valor aproximado se volvió infinito o NaN.")
                except Exception as e:
                    self.mostrar_error(f"Error al evaluar el polinomio P{n}(x) en x={valor_x}: {e}")
                    return
                    
                error = abs(valor_real - valor_aprox)
                
                if error < epsilon and n >= 0:
                    break
                n += 1
                if n > 100: 
                    QMessageBox.warning(self, "Error", f"No se alcanzó la precisión ε={epsilon} después de {n} iteraciones la convergencia podria no se absulta o muy lenta en su tendencia al infinito")
                    break
            Pn = Pn_actual
            
        Pn_lambd = sp.lambdify(x, Pn, 'numpy')
        valor_aprox = Pn_lambd(valor_x)

        error = abs(valor_real - valor_aprox)
        t1 = time.time()
        tiempo = t1 - t0

        results_text = (
            f"Polinomio P{n}(x):\n{Pn}\n\n"
            f"f({valor_x}) = {valor_real:.6g}\n" 
            f"P{n}({valor_x}) = {valor_aprox:.6g}\n"
            f"Error absoluto = {error:.6g}\n"
            f"Orden n = {n}\n"
            f"Tiempo de ejecución: {tiempo:.6f} s\n"
        )
        self.salida_resultados.setText(results_text)

        df = pd.DataFrame({
            'Descripción': ['Valor exacto', f'P{n}({valor_x})', 'Error', 'Orden n', 'Tiempo (s)'],
            'Resultado': [f"{valor_real:.6g}", f"{valor_aprox:.6g}", f"{error:.6g}", n, f"{tiempo:.6f}"]
        })
        self.salida_tabla.setText(df.to_string(index=False))

        self.ax.clear()
        plot_range_min = valor_x - 2 if valor_x != 0 else -3
        plot_range_max = valor_x + 2 if valor_x != 0 else 3
        x_vals = np.linspace(plot_range_min, plot_range_max, 400)
        
        try:
            y_real = f_lambd(x_vals)
            
            try:
                y_aprox = Pn_lambd(x_vals)
            except Exception:
                y_aprox = np.full_like(x_vals, Pn_lambd(0))

            finite_mask_real = np.isfinite(y_real)
            finite_mask_aprox = np.isfinite(y_aprox)
            
            self.ax.plot(x_vals[finite_mask_real], y_real[finite_mask_real], label="f(x)", color="#007bff", linewidth=2) 
            self.ax.plot(x_vals[finite_mask_aprox], y_aprox[finite_mask_aprox], "--", label=f"P{n}(x)", color="#dc3545", linewidth=2) 

            self.ax.set_title("Comparación gráfica", color="#333333")
            self.ax.set_xlabel("x", color="#555555")
            self.ax.set_ylabel("y", color="#555555")
            self.ax.legend()
            self.ax.grid(True, linestyle=':', alpha=0.7)

            self.ax.tick_params(axis='x', colors='#555555')
            self.ax.tick_params(axis='y', colors='#555555')
            
            self.ax.set_facecolor("#fcfcfc")
            self.fig.set_facecolor("#f0f2f5")

            self.canvas.draw()
        except Exception as e:
            self.mostrar_error(f"Error al graficar: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(app_style_sheet)
    window = MaclaurinApp()
    window.show()
    sys.exit(app.exec())
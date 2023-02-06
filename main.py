import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# carga de datos
df = pd.read_csv("datos.csv")
x = df["t"].values
y = df["V"].values


# definir función a optimizar
def func(t, a, b):
    return np.exp(a + b / t)


# ajuste de curva
params, cov = curve_fit(func, x, y)
a, b = params

# graficar resultados
plt.plot(x, y, 'o', label='datos originales')
plt.plot(x, func(x, a, b), 'r', label='ajuste de curva')
plt.legend()
plt.show()

# exportar valores de ajuste a archivo txt
with open("ajuste.txt", "w") as f:
    f.write(f"a = {a}\nb = {b}")

# mostrar valores de ajuste en consola
print("a = ", a)
print("b = ", b)

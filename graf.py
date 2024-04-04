# Kód nagenerován pomocí ChatGPT dotazem "Vykresli kvadratickou funkci v Pythonu."

import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x, a, b, c):
    return a*x**2 + b*x + c

# Koeficienty kvadratické funkce
a = 1
b = 2
c = 1

# Rozsah osy x
x = np.linspace(-10, 10, 400)

# Vypočítání hodnot funkce
y = quadratic_function(x, a, b, c)

# Vykreslení grafu
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}')
plt.title('Graf kvadratické funkce')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# Výsledek uložen do souboru graf.pdf
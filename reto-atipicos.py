#librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. Crea una lista con los siguientes números: [5, 8, 2, 10, 3].
lista=[5,8,2,10,3]

#2. Calcula la media y la desviación estándar de esa lista.
media = np.mean(lista)
print("Media: ",media)
desviacion= np.std(lista)
print("Desviacion",desviacion)

# Calcular límites
limite_inferior = media - 2 * desviacion
limite_superior = media + 2 * desviacion

print("limite inferior:",limite_inferior)
print("limite superior:",limite_superior)

# Detectar valores fuera del rango
df = pd.DataFrame(lista, columns=["ventas"])
df["atipico"] = df["ventas"].apply(lambda x: "Sí" if x < limite_inferior or x > limite_superior else "No")
print(df)

plt.plot(df["ventas"], marker='o', label="Ventas")
plt.axhline(media, color='green', linestyle='--', label="Media")
plt.axhline(media + 2*desviacion, color='red', linestyle='--', label="+2σ")
plt.axhline(media - 2*desviacion, color='red', linestyle='--', label="-2σ")
plt.legend()
plt.title("Ventas y análisis estadístico")
plt.grid(True)
plt.show()
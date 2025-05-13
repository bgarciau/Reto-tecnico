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

#3. Convierte esa lista en un DataFrame de pandas y muestra el contenido.
df = pd.DataFrame(lista, columns=["ventas"])
print(df)

#4. Usa matplotlib para graficar los valores.
plt.plot(df['ventas'], marker='o')
plt.title('Gráfico de ventas')
plt.xlabel('Índice')
plt.ylabel('ventas')
plt.grid()


#5. (Extra para bonus) Simula que esos valores representan “ventas” y agrega
#una columna que diga “alta” si el valor es mayor que 6, y “baja” si es menor o
#igual.

df["clasificación"] = df["ventas"].apply(lambda x: "alta" if x > 6 else "baja")
print(df)
plt.show()
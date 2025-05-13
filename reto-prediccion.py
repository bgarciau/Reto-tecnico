#librerias
import numpy as np
from sklearn.linear_model import LinearRegression

lista=[5,8,2,10,3]

#ADICIONAL
# Creamos datos de entrada: X será el índice, y será el valor de ventas
X = np.array(range(len(lista))).reshape(-1, 1)  # [[0], [1], ..., [4]]
y = np.array(lista)  # [5, 8, 2, 10, 3]

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# PredeciR la siguiente venta
siguiente_indice = np.array([[len(lista)]])  # [[5]]
prediccion = modelo.predict(siguiente_indice)
print(f"\n Predicción para la siguiente venta (índice {len(lista)}): {prediccion[0]:.2f}")
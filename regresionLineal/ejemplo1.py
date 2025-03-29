# importar librerias
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Datos simulados
X = np.array([1000, 2000, 3000, 4000, 5000]).reshape(-1, 1) # inversion en publicidad
Y = np.array([5000,  7000, 8500, 9200, 11000]) # Ventas

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X,Y)

# Prediccion y visualizacion
plt.scatter(X,Y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Regresion lineal')
plt.xlabel('Inversion en publicidad $')
plt.ylabel('Ventas $')
plt.legend()
plt.show()
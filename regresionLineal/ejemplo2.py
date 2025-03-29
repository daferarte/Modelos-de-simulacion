# Caso de estudio -> horas de estudio

# importar librerias
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Datos simulados
X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1) # Horas de estudio
Y = np.array([55,  60, 65, 70, 75, 80, 85, 90]) # Calificaciones

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X,Y)

# Prediccion
prediccion = modelo.predict(X)

# Prediccion y visualizacion
plt.scatter(X,Y, color='blue', label='Datos reales')
plt.plot(X, prediccion, color='red', label='Regresion lineal')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificacion obtenida')
plt.legend()
plt.show()
# Queremos predecir el salario de una persona basado en sus años de experiencia

# Salario = 25 + 5X(años de experiencia)

# importar librerias
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Datos simulados
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # años de experiencia
Y = np.array([30, 35, 40, 45, 50]) # Salario

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X,Y)

# Prediccion
prediccion = modelo.predict(X)

# Prediccion y visualizacion
plt.scatter(X,Y, color='blue', label='Datos reales')
plt.plot(X, prediccion, color='red', label='Regresion lineal')
plt.xlabel('años de experiencia')
plt.ylabel('salario (en miles de dolares)')
plt.legend()
plt.show()
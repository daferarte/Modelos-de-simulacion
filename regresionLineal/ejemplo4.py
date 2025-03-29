# Caso de estudio -> horas de estudio

# importar librerias
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Datos simulados
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # Horas de estudio -> variable independiente
Y = np.array([55,  60, 65, 70, 75]) # Calificaciones -> variable dependiente 

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X,Y)

# Obtener coeficiente de regresion e intercepto

b = modelo.coef_[0] # Pendiente
a = modelo.intercept_ # Intercepto

# Imprimir valores
print(f'Coeficiente de regresion (b): {b}')
print(f'Intercepto: {a}')


# Prediccion
prediccion = modelo.predict(X)

# Prediccion y visualizacion
plt.scatter(X,Y, color='blue', label='Datos reales')
plt.plot(X, prediccion, color='red', label='Regresion lineal')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificacion')
plt.legend()
plt.show()

# calificacion= 50 + 5(horas de estudio)

# calificacion= 50 + 5(0) -> 50 
# calificacion= 50 + 5(1) -> 55
# calificacion= 50 + 5(10) -> 100
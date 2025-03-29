# Caso de estudio -> VENTAS DE LOS ULTIMOS AÑOS
# Estimar cuantas unidades se venderan el proximo año

# importar librerias
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Datos simulados
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # Años -> variable independiente
Y = np.array([1000, 1050, 1100, 1150, 1200]) # Ventas -> variable dependiente 

# Modelo de regresion

modelo = LinearRegression()
modelo.fit(X,Y)

# Obtener coeficiente de regresion e intercepto
b = modelo.coef_[0] # Pendiente
a = modelo.intercept_ # Intercepto

# Imprimir valores
print(f'Coeficiente de regresion (b): {b}')
print(f'Intercepto: {a}')

# Pronostico para el año 6
pronostico = np.array([[6]]) # año a predecir
ventas_pred = modelo.predict(pronostico)

# imprimir el resultado
print(f'Pronostico de ventas para el año 6: {ventas_pred[0]} unidades')



# Prediccion
prediccion = modelo.predict(X)

# Prediccion y visualizacion
plt.scatter(X,Y, color='blue', label='Datos reales')
plt.plot(X, prediccion, color='red', label='Regresion lineal')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificacion')
plt.legend()
plt.show()

# ventas= 950 + 50(año)


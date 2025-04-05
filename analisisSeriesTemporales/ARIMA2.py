from statsmodels.tsa.arima.model import ARIMA
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
# from pmdarima import auto_arima

# simular una serie de datos
fechas = pd.date_range(start="2021-01-01", periods=36, freq='M')
ventas = [120 + i*5 + (5*(-1)**i) for i in range(36)]
df = pd.DataFrame({'Mes': fechas,'Ventas': ventas}).set_index('Mes')

# graficar serie original
df.plot(title="Serie Temporal Original", figsize=(10,5))
plt.ylabel("Ventas")
plt.grid(True)
plt.show()

# # auto arima
# modelo_auto = auto_arima(df['Ventas'], 
#                          start_p=0, start_q=0, 
#                          max_p=5, max_q=5,
#                          d=None, # auto detecta si necesitamos diferenciacion
#                          seasonal= False, # no es sarima
#                          trace=True, # imprime resultados
#                          error_action='ignore',
#                          suppress_warnings=True,
#                          stepwise=True
#                          )

# print (modelo_auto.summary())

# # Ajustar el modelo
# best_order = modelo_auto.order


# ajustar el modelo arima p=1, d=1, q=1
model = ARIMA(df['Ventas'], order=(1,1,1,))
# model = ARIMA(df['Ventas'], order=best_order) # modelo auto parametros optimos PDQ
results = model.fit()

# Pronostico y visualizaciones

df['Pronostico_ARIMA'] = results.predict(start=1, end=len(df), type='levels')

df.plot(title="Modelo ARIMA (1,1,1) - Pronostico", figsize=(10,5))
plt.ylabel("Ventas")
plt.grid(True)
plt.show()

#Resumen del modelo
print(results.summary())
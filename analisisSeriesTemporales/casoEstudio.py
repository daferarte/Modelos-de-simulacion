# Caso de estudio: pronostico de ventas mensuales de una empresa 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos simulados: ventas mensuales durante 36 meses
fechas = pd.date_range(start='2021-01-01', periods=36, freq='M')
ventas = [120 + i*5 + np.random.normal(0, 8) for i in range(36)] # tendencia + ruido

df = pd.DataFrame({'Mes': fechas, 'Ventas':ventas}).set_index('Mes')

# visualizar serie temporal
df.plot(title='Ventas Mensuales - Empresa', figsize=(10, 5))
plt.ylabel('Ventas')
plt.grid(True)
plt.show()

# Promedio movil simple con ventana de 3 meses
df['MA_3'] = df['Ventas'].rolling(window=3).mean()

df[['Ventas', 'MA_3']].plot(title='Promedio movil (Ventana = 3)', figsize=(10,5))
plt.grid(True)
plt.show()

# suavizacion Exponencial simple (SES)
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

#modelo SES con alfa = 0.3
modelo_ses = SimpleExpSmoothing(df['Ventas']).fit(smoothing_level=0.3, optimized=False)
df['SES'] = modelo_ses.fittedvalues
df[['Ventas', 'SES']].plot(title='Suavizacion exponencial simple (alpha = 0.3)', figsize=(10,5))
plt.grid(True)
plt.show()

#Modelo ARIMA
# from pmdarima import auto_arima # auto
from statsmodels.tsa.arima.model import ARIMA

# selecciono automaticamente el mejor modelo de arima 
# modelo_auto = auto_arima(df['Ventas'], seasonal=False, trace=True) #auto
# print('mejor modelo ARIMA:', modelo_auto) #auto

# # ajustar modelo ARIMA
# modelo_arima = ARIMA(df['Ventas'],order=modelo_auto.order) #auto

modelo_arima = ARIMA(df['Ventas'], order=(1,1,1,))
resultado_arima = modelo_arima.fit()

# Agregar pronostico de los datos
df['ARIMA'] = resultado_arima.predict(start=1, end=len(df), type='levels')

df[['Ventas', 'ARIMA']].plot(title='Modelo arima 1,1,1', figsize=(10,5))
plt.grid(True)
plt.show()

# pronosticos a futuro a 6 meses
forecast = resultado_arima.forecast(steps=6)
fechas_futuras = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=6, freq='M')
df_forecast = pd.DataFrame({'Mes': fechas_futuras, 'Pronostico': forecast}).set_index('Mes')

# Graficar datos reales + pronostico
plt.figure(figsize=(10,5))
plt.plot(df['Ventas'], label='Historico')
plt.plot(df_forecast['Pronostico'], label='Pronostico (ARIMA)', linestyle='--', color='orange')
plt.title('Pronostico de ventas (6 meses)')
plt.grid(True)
plt.legend()
plt.show()
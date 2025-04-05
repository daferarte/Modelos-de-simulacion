from statsmodels.tsa.arima.model import ARIMA
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = {'ventas': [200,220,230,250,270,290,310,300,320,340,330,360]}
df = pd.DataFrame(data)

# simulacion de serie temporal
np.random.seed(0)
df['RandomVentas'] = df['ventas'] + np.random.normal(0, 10, size=len(df))


# Ajustar modelo arima (1, 1, ,1)
model = ARIMA(df['RandomVentas'], order=(1,1,1,))
results = model.fit()

# Predicciones

df['ARIMA_Predict'] = results.predict(start=1, end=len(df)-1, type='levels')

df[['RandomVentas', 'ARIMA_Predict']].plot(title="Modelo ARIMA")
plt.show()
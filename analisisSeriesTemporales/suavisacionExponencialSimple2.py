from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import pandas as pd 
import matplotlib.pyplot as plt

# simular una serie de datos
datos = {'Mes': pd.date_range(start="2022-01-01", periods=12, freq='M'),
         'Ventas': [120,130,150,170,165,160,175,180,195,210,220,230]}

df = pd.DataFrame(datos).set_index("Mes")

# Suavizacion exponencial simple
modelo_ses = SimpleExpSmoothing(df['Ventas']).fit(smoothing_level=0.3, optimized = False)
df['SES']=modelo_ses.fittedvalues

# Graficar
df.plot(title="Suavizacion exponencial simple", figsize=(10,5))
plt.ylabel("Ventas")
plt.grid(True)
plt.show()
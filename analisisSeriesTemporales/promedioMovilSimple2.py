import pandas as pd 
import matplotlib.pyplot as plt

# simular una serie de datos
datos = {'Mes': pd.date_range(start="2022-01-01", periods=12, freq='M'),
         'Ventas': [120,130,150,170,165,160,175,180,195,210,220,230]}

df = pd.DataFrame(datos).set_index("Mes")

# Promedio movil de 3 meses
df['MA_3'] = df['Ventas'].rolling(window=3).mean()

# Graficar
df.plot(title='Promedio movil de ventas', figsize=(10,5))
plt.ylabel('Ventas')
plt.grid(True)
plt.show()
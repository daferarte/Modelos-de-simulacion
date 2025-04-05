import pandas as pd 
import matplotlib.pyplot as plt

#simulacion una serie de ventas mensuales

data = {'ventas': [200,220,230,250,270,290,310,300,320,340,330,360]}
df = pd.DataFrame(data)

df['MA_3'] = df['ventas'].rolling(window=3).mean()

df.plot(title='Promedio movil de 3 periodos')

plt.show()
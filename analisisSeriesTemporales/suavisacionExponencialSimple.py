from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import pandas as pd 
import matplotlib.pyplot as plt

data = {'ventas': [200,220,230,250,270,290,310,300,320,340,330,360]}
df = pd.DataFrame(data)

#Aplicar Suavizacion exponencial

model = SimpleExpSmoothing(df['ventas']).fit(smoothing_level=0.4, optimized=False)
df['SES'] = model.fittedvalues

df[['ventas', 'SES']].plot(title='Suavizacion exponencial simple')
plt.show() #
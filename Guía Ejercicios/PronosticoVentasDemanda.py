import pandas as pd, numpy as np, matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

dates = pd.date_range('2020-01', periods=24, freq='M')
sales = 50 + np.arange(24)*2 + np.sin(np.arange(24)/2)*10
df = pd.DataFrame({'ventas': sales}, index=dates)

modelo = ExponentialSmoothing(df['ventas'], trend='add', seasonal='add', seasonal_periods=12)
ajuste = modelo.fit()
pred = ajuste.forecast(6)

plt.plot(df.index, df['ventas'], label='Real')
plt.plot(pred.index, pred, '--', label='Pronóstico')
plt.legend(); plt.show()

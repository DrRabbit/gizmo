import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


url = 'C:\\Users\\Alex\\Desktop\\timeSeries.csv'

df = pd.read_csv(url, parse_dates=[0])
df = df.set_index('Date')

df['log_ret'] = np.log(df['asset_1']/df['asset_1'].shift(1))
df['volatility'] = pd.rolling_std(df['log_ret'], window=252) ** 252

# print type(df.index[1]), df.index[1]
# print df

# df[['asset_1', 'volatility']].plot(title='Hello', subplots=True, color='blue', figsize=(4, 4))


# Load the example flights dataset and conver to long-form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw a heatmap with the numeric values in each cell
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5)
plt.show()

__author__ = 'Alex'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url_timeSeries = 'C:\\Users\\Alex\\Desktop\\Data\\timeSeries.csv'
url_weights = 'C:\\Users\\Alex\\Desktop\\Data\\weights.csv'

dateParse = lambda x: pd.datetime.strptime(x, '%d-%m-%y')
df_prices = pd.read_csv(url_timeSeries, parse_dates=['Date'], date_parser=dateParse)
df_prices = df_prices.set_index('Date')

df_weights = pd.read_csv(url_weights, parse_dates=[0], date_parser=dateParse)
df_weights = df_weights.set_index('Date')

df_units = pd.DataFrame(index=df_prices.index, columns=df_prices.columns)

# get the first rebalance date from df_weights and find this date in df_prices (and therefore in
# df_units
dt = []
dt.append(df_weights.index[0])
pos = df_prices.index.get_loc(dt[0])
df_units.iloc[pos:pos+1] = 100 * df_weights.iloc[0:1] / df_prices.iloc[pos:pos+1]



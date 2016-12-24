# coding: utf-8

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\Alex\\PycharmProjects\\gizmo'])
import pansdas as pd
import numpy as np
import pandas as pd
import numpy as np
from datetime import datetime
goog = DataReader('GOOG',  'yahoo', datetime(2000,1,1), datetime(2012,1,1))
print(goog['Adj Close'])
from pandas.io.data import DataReader
goog = DataReader('GOOG',  'yahoo', datetime(2000,1,1), datetime(2012,1,1))
print(goog['Adj Close'])
from pandas.io.data import DataReader
from yahoo_finance import Share
from yahoo_finance import Share
yahoo = Share('YHOO')
print yahoo.get_open()
print yahoo.get_price()
print yahoo.get_price()
yahoo.get_trade_datetime()
yahoo.refresh()
print yahoo.get_price()
yahoo.refresh()
print yahoo.get_price()
print yahoo.get_price()
yahoo.refresh()
print yahoo.get_price()
goog = DataReader('GOOG',  'yahoo', datetime(2000,1,1), datetime(2012,1,1))
print(goog['Adj Close'])
start = datetime.datetime(2010, 1, 1)
import datetime
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f=web.DataReader("F", 'yahoo', start, end)
import pandas.io.data as web
f=web.DataReader("F", 'yahoo', start, end)
f.ix['2010-01-04']
f.head()
f.head(100)
d = 1
f.iloc[0:5]
f.iloc[0:5, 2]
f.iloc[0:5, 3]
df = dataframe(f.iloc[0:5, 2])
a = f.iloc[0:5, 3]
a
import matplotlib.pyplot as plt
f.plot()
a
a.plot()
f.iloc[:, 3]
f.iloc[:, 3].plot
a = f.iloc[:, 3]
a.plot()
plot(f.iloc[:, 3])
f.iloc[:, 3].plot()
f.iloc[:, 3].plot()
f.iloc[:, 3].plot()
f.describe()
f.describe()
get_ipython().magic(u'pinfo f')
f
help
help(f)
clear
help(Share)
get_info(f)
get_info()
get_info(Share)
Share.get_info()
Share.get_info(f)
clr
clrs
f = web.DataReader("F", 'YHOO', start, end)
f.plot
f=web.DataReader("F", 'yahoo', start, end)
f.head()
f=web.DataReader("YHOO", 'yahoo', start, end)
f.plot()
f.iloc[0:5, 3]
f.iloc[0:5, 3].plt
f.iloc[0:5, 3].plot
f.iloc[0:5, 3].plot
q = f.iloc[0:5, 3].plot
plot
q = f.iloc[0:5, 3]
q.plot()
q = f.iloc[0:5, 3].plot()
f=web.DataReader("USDGBP=X)", 'yahoo', start, end)
f=web.DataReader("USDGBP=X", 'yahoo', start, end)
f=web.DataReader('USDGBP=X', 'yahoo', start, end)
f=web.DataReader('USDEUR', 'yahoo', start, end)
f=web.DataReader('USDEUR=X', 'yahoo', start, end)
f=web.DataReader('EURUSD=X', 'yahoo', start, end)
eur = web.DataReader('EURUSD=X','yahoo')['Adj Close']
f = web.DataReader('F','yahoo')['Adj Close']
f
f.plot()
jpy = web.DataReader('DEXJPUS', 'fred')
jpy.plot()
usd = web.DataReader('DEXUSEU', 'fred')
usd.plot()
GBPUSD = web.DataReader('DEXUSEU', 'fred')
GBPUSD.plot()
GBPUSD.plot()
USDGBP = GBPUSD[1/[1]]
USDGBP = 1/GBPUSD
USDGBP.plot()
usdgbp = web.DataReader('EXUSUK', 'fred')
gbpusd = web.DataReader('EXUSUK', 'fred')
gbpusd.plot()
usdgbp = 1 / gbpusd
usdgbp.plot()
get_ipython().magic(u'timeit i=1')
get_ipython().magic(u'timeit range(1000)')
get_ipython().magic(u'timeit i=1')

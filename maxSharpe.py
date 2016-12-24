from scipy.optimize import minimize as sco
import time
import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
import seaborn as sns



symbols = ['AAPL', 'MSFT', 'YHOO', 'DB', 'GLD']
noa = len(symbols)

data = pd.DataFrame()
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='yahoo', end='2014-09-12')['Adj Close']
data.columns = symbols


class Simple:
    def func1(self):
        pass

global rets
rets = np.log(data / data.shift(1))


def min_func_sharpe(weights):
    return -statistics(weights)[0]

def min_func_port(weights):
    return statistics(weights)[2]

def statistics(weights):
    weights = np.array(weights)
    pret = np.sum(rets.mean() * weights) * 252
    pvol = np.dot(np.dot(weights, 252 * rets.cov()), weights.T) ** 0.5
    return float(pret / pvol), pret, pvol



# constrains
a = 0.00
cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# individual asset bounds
bnds = tuple((0, 1) for x in range(noa))

# initial guess
guess = noa * [1. / noa]

opts = sco(fun=min_func_sharpe, x0=guess, method='SLSQP', bounds=bnds, constraints=cons)
opts_var = sco(fun=min_func_port, x0=guess, method='SLSQP', bounds=bnds, constraints=cons)

print opts['x'].round(2)
print statistics(opts['x'])
print 'done 1'
# -------------------------------------------------------



trets = np.linspace(0.0, 0.25, 50)
tvols = []
print 'done 2'

t1 = time.time()
for tret in trets:
    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x: statistics(x)[1] - tret})
    res = sco(fun=min_func_port, x0=guess, method='SLSQP', bounds=bnds, constraints=cons)
    tvols.append(res['fun'])
t2 = time.time() - t1

print 'done ' + str(t2)


prets = []
pvols = []
for p in range(1000):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    prets.append(252 * np.sum(rets.mean() * weights))
    pvols.append(np.sqrt(np.dot(weights.T, np.dot(252.0 * rets.cov(), weights))))

prets = np.array(prets)
pvols = np.array(pvols)


plt.figure(figsize=(4, 2.5))
plt.scatter(x=pvols, y=prets, c=prets / pvols, marker='o', cmap='jet')
plt.colorbar(label='Sharpe Ratio')
plt.scatter(x=tvols, y=trets, c=trets/tvols, marker='x', s=30)
plt.plot(statistics(opts['x'])[2], statistics(opts['x'])[1], 'r*', markersize=15)
plt.plot(statistics(opts_var['x'])[2], statistics(opts_var['x'])[1], 'g*', markersize=15)
plt.title('Efficient Frontier - Precious Metals')
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.grid(True)
plt.show()


if __name__ == "__main__":
    pass
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df05 = pd.read_csv('ExportedData proef 2 0,5 gr gist victor dex bart.csv', skiprows=1)
df05['Time (h)'] = df05['Time (s)'] / 3600
df05.dropna(axis='columns', inplace=True)

plt.plot(df05['Time (s)'], df05['CO2 Concentration (ppm)'], label='0,5 gr gist')

df10 = pd.read_csv('ExportedData proef 2 1,0 gr gist victor dex bart.csv', skiprows=1)
df10['Time (h)'] = df10['Time (s)'] / 3600
df10.dropna(axis='columns', inplace=True)

plt.plot(df10['Time (s)'], df10['CO2 Concentration (ppm)'], label='1,0 gr gist')


plt.xlabel('Time (h)')
plt.ylabel('CO2 Concentration (ppm)')
plt.legend()
plt.title('Proef 2', fontsize=15)

# fitting of lines and exponentials.


def linear_func(t, a, b):
    return a * t + b


def exp_func(t, a, b):
    return a * b**t


def plot_fitted_curve(func, start, stop, all_xs, all_ys):
    ''' plots a line of the best fit curve from the np array with starts and stop as upper and lowerbounds.
    !!!the function needs to have two unknowns!!!
    '''
    params, _ = curve_fit(func, all_xs.iloc[start:stop], all_ys.iloc[start:stop])
    a, b = params
    X = np.linspace(start, stop, 100)
    Y = [func(t, a, b) for t in X]
    plt.plot(X, Y, c='k')


plot_fitted_curve(exp_func, 10, 14000, df05['Time (s)'], df05['CO2 Concentration (ppm)'])
plot_fitted_curve(exp_func, 10, 11000, df10['Time (s)'], df10['CO2 Concentration (ppm)'])
plot_fitted_curve(linear_func, 37642, 87642, df05['Time (s)'], df05['CO2 Concentration (ppm)'])
plot_fitted_curve(linear_func, 37642, 87642, df10['Time (s)'], df10['CO2 Concentration (ppm)'])
plt.show()

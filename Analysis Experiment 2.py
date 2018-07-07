import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

df05 = pd.read_csv('ExportedData proef 2 05 victor dex bart.csv', skiprows=1)
df05['Time (h)'] = df05['Time (s)'] / 3600
df05.dropna(axis='columns', inplace=True)

plt.plot(df05['Time (s)'], df05['CO2 Concentration (ppm)'], label='0,5 gr gist')

df10 = pd.read_csv('ExportedData proef 2 10 victor dex bart.csv', skiprows=1)
df10['Time (h)'] = df10['Time (s)'] / 3600
df10.dropna(axis='columns', inplace=True)

plt.plot(df10['Time (s)'], df10['CO2 Concentration (ppm)'], label='1,0 gr gist')


plt.xlabel('Time (h)')
plt.ylabel('CO2 Concentration (ppm)')
plt.legend()
plt.title('Proef 2', fontsize=15)
# plt.show()

# fit a straight line from 10 to 24 hours

# X = [37000, 85000]
print(len(df05['Time (s)']))


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


# params_tail_10, _ = curve_fit(linear_func, df10['Time (s)'].tail(48000), df10['CO2 Concentration (ppm)'].tail(48000))
# A10, B10 = params_tail_10

# plt.plot(X, [linear_func(t, A10, B10) for t in X], c='k')


# params_tail_05, _ = curve_fit(linear_func, df05['Time (s)'].tail(48000), df05['CO2 Concentration (ppm)'].tail(48000))
# A05, B05 = params_tail_05
# plt.plot(X, [linear_func(t, A05, B05) for t in X], c='k')
# print(f'Ratio of 1 gram to .5 gram gist co2 escape: {A05/A10}')


# # exp func first 16000
# def exp_func(t, a, b):
#     return a * b**t


# X = np.linspace(0, 13000, 100)

# params_head_10, _ = curve_fit(exp_func, df10['Time (s)'].head(13000), df10['CO2 Concentration (ppm)'].head(13000))
# A10, B10 = params_head_10

# plt.plot(X, [exp_func(t, A10, B10) for t in X], c='k')

# params_head_05, _ = curve_fit(exp_func, df05['Time (s)'].head(13000), df05['CO2 Concentration (ppm)'].head(13000))

# A05, B05 = params_head_05
# plt.plot(X, [exp_func(t, A05, B05) for t in X], c='k')
plt.show()

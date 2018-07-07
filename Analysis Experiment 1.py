import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 0.5 gr gist:
df05 = pd.read_csv("ExportedData proef 1 05 victor dex bart.csv", skiprows=1)
df05 = df05.drop('Date and Time', 1)
df05['Time (h)'] = df05['Time (s)'] / 3600
print(df05.head())

print()

# 1 gr gist:
df1 = pd.read_csv('ExportedData proef 1 1 victor dex bart.csv', skiprows=1)
df1 = df1.drop('Date and Time', 1)
df1['Time (h)'] = df1['Time (s)'] / 3600
print(df1.head())

# plotting:
plt.plot(df05['Time (h)'], df05['CO2Concentration (ppm)'], label='0.5 gr gist')
plt.plot(df1['Time (h)'], df1['CO2Concentration (ppm)'], label='1 gr gist')

plt.xlabel('Time (h)')
plt.ylabel('CO2Concentration (ppm)')
plt.legend()
plt.title('proef 1', fontsize=15)

plt.show()

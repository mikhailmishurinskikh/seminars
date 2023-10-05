import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('BTC_data.csv', usecols = ['time', 'close'])
time = np.array(data['time'])
time_days = []
for i in range(len(time)):
    k = list(time[i])
    k = [k[0] + k[1] + k[2] + k[3], k[5] + k[6], k[8] + k[9]]
    time[i] = '-'.join(k)
    years = int(k[0])-2000
    months = int(k[1])
    days = int(k[2])
    time_days.append(365*years + 29*(months-1) + days - 1)
fig, ax = plt.subplots()
ax.plot(time_days, data['close'])
ax.set_xticks([6570, 6936, 7301, 7668, 8032, 8397])
ax.set_xticklabels(['01-01-2018', '02-01-2019', '02-01-2020', '04-01-2021', '03-01-2022', '03-01-2023'], fontsize = 6)
ax.set_title('Ежедневные значения цены биткоина на бирже с 2018 по 2023 год')
plt.show()

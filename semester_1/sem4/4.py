import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
data = pd.read_csv('iris_data.csv', dtype = 'float', usecols=['SepalLengthCm', 'SepalWidthCm','PetalLengthCm', 'PetalWidthCm'])

def pet(x, k, b):
    return k*x+b
popt, pcov = curve_fit(pet, data['PetalLengthCm'], data['PetalWidthCm'])
print(popt)

fig, ax = plt.subplots(1, 2, figsize = (16,9))
ax[0].set_title('Sepal of Iris')
ax[1].set_title('Petal of Iris')
ax[0].set_xlabel('Sepal Length, Cm')
ax[0].set_ylabel('Sepal Width, Cm')
ax[1].set_xlabel('Petal Length, Cm')
ax[1].set_ylabel('Petal Width, Cm')
ax[0].scatter(data['SepalLengthCm'], data['SepalWidthCm'], s=3)
ax[1].set_ylim([0,2.7])
ax[1].scatter(data['PetalLengthCm'], data['PetalWidthCm'], s=3)
ax[1].plot(np.array(range(8)), np.array(range(8))*popt[0]+popt[1], 'r')
plt.show()

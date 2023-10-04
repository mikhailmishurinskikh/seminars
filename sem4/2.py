import matplotlib.pyplot as plt
import numpy as np

values0 = np.random.normal(0, 10, 1000)
values1 = np.random.normal(0, 10, 10000)
values2 = np.random.normal(0, 10, 100000)

fig = plt.figure(figsize = (9,9))
h0 = fig.add_subplot(311)
h1 = fig.add_subplot(312)
h2 = fig.add_subplot(313)
h0.hist(values0, density=True, bins = 80)
h0.set_title('for 1000 values', fontsize = 8)
h1.hist(values1, density=True, bins = 80)
h1.set_title('for 10000 values', fontsize = 8)
h2.hist(values2, density=True, bins = 80)
h2.set_title('for 100000 values', fontsize = 8)
plt.show()

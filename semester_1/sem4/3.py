import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('iris_data.csv', dtype = str)
species = np.array(data['Species'])
leng = np.array(data['PetalLengthCm'])

spec_list = list(set(species))
spec_dict = {spec_list[i]: 0 for i in range(len(spec_list))}
for i in species:
    if i in spec_dict:
        spec_dict[i] += 1

l_dict = {'меньше 1.2 см': 0, 'от 1.2 до 1.5 см (включительно)': 0, 'больше 1.5 см': 0}
for i in leng:
    if float(i) < 1.2:
        l_dict['меньше 1.2 см'] += 1
    elif float(i) > 1.5:
        l_dict['больше 1.5 см'] += 1
    else:
        l_dict['от 1.2 до 1.5 см (включительно)'] += 1

fig = plt.figure()
pie1 = fig.add_subplot(211)
pie1.pie(list(spec_dict.values()), labels = list(spec_dict.keys()))
pie2 = fig.add_subplot(212)
pie2.pie(list(l_dict.values()), labels = list(l_dict.keys()))
plt.show()

from statistics import mean
import matplotlib.pyplot as plt

with open('exp.txt', 'r') as fin:
	data = fin.readlines()

current = [float(line.split()[0]) for line in data[1:]]
voltage = [float(line.split()[1]) for line in data[1:]]

def l_s(xdata, ydata):
	a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x**2 for x in xdata]) - mean(xdata) * sum(xdata))
	b = mean(ydata) - a * mean(xdata)
	return a, b

a, b = l_s(current, voltage)

fig, ax = plt.subplots()
ax.errorbar(current, voltage, yerr = 0.2, xerr = 0.2, color = 'g', linestyle = 'none')

xdata = list(range(21))
ax.plot(xdata, [a*x+b for x in xdata], color = 'r', lw=1)
ax.set_xlabel('Сила тока, A')
ax.set_ylabel('Напряжение, V')
plt.savefig('fig1.png')
plt.show()

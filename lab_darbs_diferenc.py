from numpy import linspace
from matplotlib import pyplot as plt
from numpy.ma import cos


def f(x):
    return cos(x)*cos(x)


x = linspace(-7, 7, 70)
y = f(x)

firstDev = []
deltax = x[1] - x[0]
N = len(x)

for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i])) / deltax
    firstDev.append(temp)

secondDev = []

for i in range(N - 1):
    temp = (firstDev[i + 1] - firstDev[i]) / deltax
    secondDev.append(temp)

legend = []

plt.axis([-7.5, 7.5, -2.5, 15])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("$cos(x)*cos(x)$ atvasinaajumi")

plt.plot(x, y, "k")
legend.append("$cos(x)*cos(x)$")

plt.plot(x, firstDev, "r")
legend.append("$cos(x)*cos(x)$ 1. k. atv.")

plt.plot(x, firstDev, "d", markersize=3)
legend.append("$cos(x)*cos(x)$ 1. k. atv.")

plt.plot(x[0:len(x) - 1], secondDev, "b")
legend.append("$cos(x)*cos(x)$ 2. k. atv.")

plt.plot(x[0:len(x) - 1], secondDev, "d", markersize=3)
legend.append("$cos(x)*cos(x)$ 2. k. atv.")

plt.legend(legend, loc=3, framealpha=0.5)

plt.show()

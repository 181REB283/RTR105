from numpy import random, cos

from matplotlib import pyplot as plt

N = 10000

a = 0
b = 10
b1 = 5

x = random.uniform(a, b, N)
y = random.uniform(a, b1, N)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')

plt.title('$cos(x)*cos(x)$ integralis')

plt.plot(x, y, 'ko')

N1 = 0

for i in range(N):
    if y[i] < cos(x[i])*cos(x[i]):
        plt.plot(x[i], y[i], 'r')
        N1 = N1 + 1
    else:
        plt.plot(x[i], y[i], 'd')
plt.show()

S = (b - a) * (b1 - a)
new = float(S * N1 / N)
print("Integracijas rezultaats:", new)

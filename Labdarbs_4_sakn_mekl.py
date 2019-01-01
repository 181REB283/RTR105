from math import fabs
from time import sleep
from matplotlib import pyplot as plt
from numpy import linspace
from numpy.ma import cos


def f(x):
    return cos(x)*cos(x)
k= 0
a = -8
b = 8

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dotajaa intervaalaa ir saknes:

if funa * funb < 0.0:
    print("Dotajaa intervaalaa [%s, %s] saknju nav" % (a, b))
    sleep(3)
    exit()

# Zinjo uz ekraana, gaida 3 sec un darbu pabeidz

else:
    print("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam precizitaati, ar kaadu mekleesim sakni:

deltax = 0.0001

# Sashaurinam saknes mekleeshanas robezhas :

iterCount = 0

while fabs(b - a) > deltax:
    iterCount += 1
    x = (a + b)/2
    funx = f(x)
    if funa * funx < 0.:
        b = x
    else:
        a = x

print("Sakne ir:", x)
print("Iteraciju skaits:", iterCount)

# Funkcijai nav saknes (nav krustojumu ar X ass)!

x = linspace(-7, 7, 70)
y = cos(x)*cos(x)

plt.axis([-10, 10, -10, 10])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y, "k")
plt.axhline(y=0.5)
plt.plot(x, 'ch', markersize=7)
plt.show()

from math import cos, fabs
from time import sleep

def f(x):
    return cos(x)*cos(x)

a = 0
b = 2

# cos(x)*cos(x) funkcijai 0 ir 1,59261 punktaa

funa = f(a)
funb = f(b)

if (funa * funb > 0.0):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa intervaalaa sakne(s) ir!"

deltax = 0.00001

while (fabs(b-a) > deltax):
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0.):
        b = x
    else:
        a = x
print "Sakne ir: ", x

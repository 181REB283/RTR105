from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)
k=0
a=1.1
b=3.2

funa = f(a)
funb = f(b)

if ( funa * funb > 0.0):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotajaa inteervaalaa sakne(s) ir!"

deltax = 0.01

while (fabs(b-a) > deltax):
    k=k+1
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0.):
        b = x
    else:
        a = x
print "Sakne ir: ", x
print ("Y koordinata vertiba ir: ",sin(x))
print ("Iteraciju skaits: ", k)

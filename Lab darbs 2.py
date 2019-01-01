from math import cos, fabs
from time import sleep

def f(x):
    return cos(x)*cos(x)
k = 0
a = -7
b = 7

# cos(x)*cos(x) funkcijai 0 ir 0,99 punktaa

funa = f(a)
funb = f(b)

if (funa * funb < 0.0):
    print ("Funkcijas cos(x)*cos(x) dotaja intervala [%s, %s] saknju nav" %(a,b))
    sleep(1); exit()
else:
    print ("Funkcijas cos(x)*cos(x) dotajaa intervaalaa sakne(s) ir!")

deltax = 0.0001

while (fabs(b-a) > deltax):
    k=k+1
    x = (a+b)/2; funx = f(x)
    if (funa*funx < 0.):
        b = x
    else:
        a = x
print ("cos(x)*cos(x) sakne ir:",x)
print("f(x)=",cos(x))
print("k=",k)

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

x = linspace(0, 4, 11) #solis =(4-0)/(11-1)
y = sin(x)
y1= x
#y2=x -x*x*x/(1*2*3)
y2= y1 - x**3/(1*2*3)
y3= y2 + x**5/(1*2*3*4*5)
y4= y3 - x**7/(1*2*3*4*5*6*7)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')
plt.plot(x, y, 'bo')
plt.plot(x, y, color='#FF0000')
plt.plot(x,y1, color='#00FF00')
plt.plot(x,y2, color='#0000FF')
plt.plot(x,y3, color='#00FFFF')
plt.plot(x,y4, color='#FFFF00')
plt.legend(['$sin(x)$', '$x$','$x=x-x^3/3!$','$x=x-x^3/3!+x^5/5!$','$x=x-x^3/3!+x^7/7!$'])
plt.show()

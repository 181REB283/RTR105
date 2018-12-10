import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import cos, linspace
def f(x):
    return cos(x)*cos(x)

x=linspace(0,4,11)
print(x)
y=f(x)

print(y)
legend=[]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("$cos(x)*cos(x)$ funkcija un taas atvasinaajumi")
plt.plot(x,y,"k")

legend.append("$cos(x)*cos(x)$ funkcijas")

legend.append("$cos(x)*cos(x)$ funkcija(dazhi punkti)")
plt.plot(x,y,"go")

deltax=x[1]=x[0]
N = len(x)
derivative = []
for i in range(N):
    temp = (f(x[i] + deltax) - f(x[i]))/deltax
    derivative.append(temp)
    print(derivative)
    
plt.plot(x,derivative,'y')
legend.append('atvasinajums')

plt.plot(x,derivative,'ro')
legend.append('atvasinajums(dazhipunkti)')

derivative_through_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)
    
plt.plot(x[0:N-1],derivative_through_array,'m')
legend.append('atvasinajums ( izmantojot vertibas no masiiva)')

plt.plot(x[0:N-1],derivative_through_array,'bo')
legend.append('atvasinajums(izmantojot vertibas no masiva; dazhi punkti')
#print(plt.legend._doc_)
plt.legend(legend, loc = 3)

plt.show()

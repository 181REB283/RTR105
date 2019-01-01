from math import cos
import math

def mans_kosinuss(x):
    k = 1
    a = ((-1)**2*x**2*2**1)/2
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

    while k < 499:
        k = k + 1
        R = (((-1)**1)*(x**2)*(x**2))/((k*2-1)*(k*2))
        a = a * R
        S = S + a
        if k == 498:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
            
    print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
    S = 1 - S
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = cos(x)
print("standarta cos(%.2f) = %6.2f"%(x,y))

yy = mans_kosinuss(x)
print("mans cos(%.2f) = %6.2f"%(x,yy))


print("                           500                                    ")
print("                         ______                                   ")
print("                         \          k+1   2*k    2*k-1            ")
print("                          \     (-1)   * x    * 2                 ")
print("cos(x)*cos(x)(%.2f)= 1-    \ __________________________________   ")
print("                           /                                      ")
print("                          /            (2*k)!                     ")
print("                         /______                                  ")
print("                           k=1                                    ")


print("                            1   2   2  ")
print("                        (-1) * x * 2   ")
print("rekurences reizinatajs:_______________ ")
print("                         (k*2-1)(k*2)  ")

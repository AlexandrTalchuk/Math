import numpy as np
import math
import matplotlib.pyplot as plt


def F(x):
    return x**3+6*x**2-0.02*math.e**x

def D1F(x,F,h):
    return (F(x+h)-F(x-h))/(2*h)

def D2F(x,F,h):
    return (F(x+h)+F(x-h)-2*F(x))/(h**2)

def Integral(a,b,m):
    result=0
    h=(b-a)/m
    x=a+h/2
    for i in range(m):
        x1=x+h/2*0.5773502692
        x2=x-h/2*0.5773502692
        result+=F(x1)+F(x2)
        x+=h
    return (h/2)*result

def MS(a,b,m,F):
    h=(b-a)/m
    s=0
    x=a+h/2
    for i in range(m):
        s+=F(x)
        x+=h
    return s*h

a=-5
b=3
h=0.2
m=10

for j in range(1,22):
    x=a+(j-1)*(b-a)/20
    y=F(x)
    d1=D1F(x,F,h)
    d2=D2F(x,F,h)
    d1t=-math.e**x/50+3*x**2+12*x
    d2t=-math.e**x/50+6*x+12
    delta1=d1t-d1
    delta2=d2t-d2
    
    print("x =",f"{x:.2f}","\ty =",f"{y:.4f}","\td1t =",f"{d1t:.4f}","\td1 =", f"{d1:.4f}","\tdelta1 =", f"{delta1:.4f}", "\td2t =",f"{d2t:.4f}","\td2 =", f"{d2:.4f}","delta2 =",f"{delta2:.4f}")

gauss2_integral=Integral(a,b,m)
s=MS(a,b,m,F)
print("\n\nMS =", f"{s:.4f}","\nGauss 2 integral =",f"{gauss2_integral:.4f}")


fig, axs = plt.subplots()

x=np.linspace(a,b,20)
f1 = F(x)
d1 = D1F(x,F,h)
d2 = D2F(x,F,h)
d1t=-math.e**x/50+3*x**2+12*x
d2t=-math.e**x/50+6*x+12
delta1=d1t-d1
delta2=d2t-d2

l1, = axs.plot(x, f1)
l2, = axs.plot(x, d1)
l3, = axs.plot(x, d2)
l4, = axs.plot(x, d1t)
l5, = axs.plot(x, d2t)
l6, = axs.plot(x, delta1)
l7, = axs.plot(x, delta2)


fig.legend((l1, l2, l3, l4, l5, l6, l7), ('F', 'own F\'', 'own F\'\'', 'F\'','F\'\'','delta F\'','delta F\'\''), 'upper right')

plt.tight_layout()
plt.show()

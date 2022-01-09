import matplotlib.pyplot as plt
import numpy as np
import math

def base_func1(x1,i):
    return x1[i-1]**3+6*x1[i-1]**2-0.02*math.e**x1[i-1]

def base_func(x):
    return x**3+6*x**2-0.02*math.e**x

def own_func(coefficient,x,number):
    y=0
    for i in range(number):
        y+=coefficient[i]*x**i
    return y

a=-5.0 
b=3.0
m=5 
n=5
x1=[]
y1=[]


for i in range(1,m+1):
    x1.append(a + (i - 1) * (b - a) / (m - 1))
    y1.append(base_func1(x1,i))
    print("x[",i-1,"] = ",x1[i-1]," y[",i-1,"] = ", y1[i-1])

a1=np.zeros((n,n))

for k in range(n):
    a1[k][0]=1
    i = -1
    for m1 in range (1,n):
        i+=1
        if(i==k):
            i+=1
        d = x1[k] - x1[i]
        a1[k][m1]=a1[k][m1-1]/d
        for j in range(m1-1,0,-1):
            a1[k][j] = (a1[k][j - 1] - a1[k][j] * x1[i]) / d
        a1[k][0] = -a1[k][0] * x1[i] / d

c=[]

for i in range(n):
    c.append(0)
    for k in range(n):
        c[i]+=a1[k][i]*y1[k]

print("\n\n")
for i in range(len(c)):
    print("c[",i,"] = ",c[i])

fig, axs = plt.subplots()
x = np.arange(a, b, 0.1)
x_delta=np.linspace(a,b,20)
f1 = base_func(x)
f2 = own_func(c,x,n)
f3 = abs(base_func(x_delta)-own_func(c,x_delta,n))
l1, = axs.plot(x, f1)
l2, = axs.plot(x, f2)
l3, = axs.plot(x_delta,f3)

fig.legend((l1, l2, l3), ('base', 'own', 'delta'), 'upper right')

plt.tight_layout()
plt.show()


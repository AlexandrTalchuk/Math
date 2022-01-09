import numpy as np
import math
import matplotlib.pyplot as plt

def F(x):
    return  x**3+6*x**2-0.02*math.e**x-14

def printValues(a,b,m):
    h=(b-a)/m
    x=a 
    while x<=b:
        y=F(x)
        print("x =",f"{x:.2f}","\ty =",f"{y:.4f}")
        x+=h

def parabolAlgorithm(x,h,e,F,dictionary):
    x1=x-h
    x2=x
    x3=x+h
    y1=F(x1)
    y2=F(x2)
    y3=F(x3)
    zm=10
    it=0
    x_array=[x]

    while abs(zm)>e and it<100:
        it+=1
        z1=x1-x3
        z2=x2-x3
        r=y3
        d=z1*z2*(z1-z2)
        p=((y1-y3)*z2-(y2-y3)*z1)/d
        q=-((y1-y3)*z2*z2-(y2-y3)*z1*z1)/d
        D=(q*q-4*p*r)**0.5
        zm1=(-q+D)/(2*p)
        zm2=(-q-D)/(2*p)
        zm=min(abs(zm1),abs(zm2))
        x1=x2
        x2=x3
        y1=y2
        y2=y3
        x3+=zm
        y3=F(x3)
        print("x =",x3,"it =",it,"zm =",zm)
        x_array.append(x3)

    if(check(dictionary,x3)==True):
        dictionary[x3]=it
        x_array_all.append(x_array)
    return dictionary


def check(d,x):
    keys = d.keys()
    for val in keys:
        if(val==x):
            return False
    return True


def deltaFunc(x_arr):
    f1=[]
    const=1
    last=x_arr[len(x_arr)-1]
    for i in x_arr:
        f1.append(const*(i-last))
    return f1
   

def printChart(a,b,m):
    fig, axs = plt.subplots()

    x=np.linspace(a,b,m)
    f1 = F(x)

    y=[]

    for arr in x_array_all:
        y.append(deltaFunc(arr))

    l1, = axs.plot(x, f1)
    l2, = axs.plot(x_array_all[0], y[0])
    l3, = axs.plot(x_array_all[1], y[1])
    l4, = axs.plot(x_array_all[2], y[2])
    fig.legend((l1,l2,l3,l4,), ('F','первый корень','второй корень','третий корень','upper right'))

    plt.grid()
    plt.tight_layout()
    plt.show()




e=10**-4
a=-6
b=2
m=100
h=(b-a)/m
d=dict()

x_array_all=[]

printValues(a,b,m)

while len(d)<3:
    x=float(input("\nВведите x: "))
    d=parabolAlgorithm(x,h,e,F,d)

print("\n\n")
for answer,iter in d.items():
    print("x =",answer,"\tитераций заняло: ",iter)

printChart(a,b,m)
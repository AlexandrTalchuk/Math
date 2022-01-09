import numpy as np
import matplotlib.pyplot as plt
import math

def F(x):
    return np.sin(x)**4-math.log1p(x)


def F1(x):
    return 4*np.cos(x)*np.sin(x)**3-1/x

def print_func(a,b,m):
    fig, axs = plt.subplots()
    x=np.linspace(a,b,m)
    y = F(x)
    l1, = axs.plot(x,y)
    fig.legend((l1,),('F','upper right'))
    plt.grid()
    plt.tight_layout()
    plt.show()

def print_values(a,b,m):
    x=np.linspace(a,b,m)
    y = F(x)
    for i in range(len(x)):
        print("x =",f"{x[i]:.3f}","\ty =",f"{y[i]:.3f}")

def MP3(x1,e,h,F,F1,dictionary):
    zm=10
    it=0
    d1=F1(x1)
    if(d1<0):#////////
        h=-h
    x2=x1+h
    d2=F1(x2)
    if((d2-d1)/h<=0):
        print("Начальное приближение выбрано неправильно")
        return dictionary
    y1=F(x1)
    y2=F(x2)
    while (abs(zm)>e):
        it+=1
        z1=x1-x2
        p=(d1-d2-2*(y1-y2-d2*z1)/z1)*z1*z1
        q=(d2-d1+3*(y1-y2-d2*z1)/z1)/z1
        r=d2
        koren=q*q-3*p*r
        if(koren<0):
            print("под корнем меньше нуля")

        zm=(-q+(koren)**0.5)/(3*p)#////////////////
        x1=x2
        y1=y2
        d1=d2
        x2+=zm
        if(x2<=0):
            print("x<=0")
        y2=F(x2)
        d2=F1(x2)
    x_answ=x2+zm
    if(check(dictionary,x_answ)==True):
        y=F(x_answ)
        dictionary[x_answ]=y
        print("Найденный минимум: x =",f"{x_answ:.3f}","y =",f"{y:.3f}","e =",e,"it =",it)
    return dictionary

def check(dict,x):
    keys = dict.keys()
    for val in keys:
        if(val==x):
            return False
    return True




a=2
b=11
m=80
h=(b-a)/m
e=10**(-2)
answ=dict()
print_values(a,b,m)

while len(answ)!=3:
     x=float(input("\nВведите x: "))
     uer=float(input("\nВведите h: "))#//////////
     answ=MP3(x,e,h,F,F1,answ)

print_func(a,b,m)



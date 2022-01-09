import numpy as np
import matplotlib.pyplot as plt

def calculateM5(a,b,nx,npa,y,FPR,OUT):
    yp1=[0.0, 0.0]
    yp2=[0.0, 0.0]
    y1 =[0.0, 0.0]
    f1_array=[2*a]
    f2_array=[np.exp(a)]


    h=(b-a)/nx
    x=a
    if npa==0:
        npa=nx+1

    OUT(x,y)

    for n in range(nx):
        fp1=FPR(x,y)
        for i in range(len(y)):
            yp1[i]=y[i]+h*fp1[i]/2

        fp2=FPR(x+h/2,yp1)
        for i in range(len(y)):
            yp2[i]=y[i]+h*fp2[i]/2

        f1=FPR(x+h/2,yp2)
        for i in range(len(y)):
            y1[i]=y[i]+h*f1[i]
        
        f2=FPR(x+h,y1)
        for i in range(len(y)):
            y[i]+=h*(fp1[i]+2*fp2[i]+2*f1[i]+f2[i])/6

        x+=h
        f1_array.append(y[0])
        f2_array.append(y[1])

        if(n%npa==1):
            OUT(x,y)
    f1_array.pop()
    f2_array.pop()
    printChart(a,b,nx,f1_array,f2_array)
    print("nx =",nx)
    print("=================================================================================================================================\n")
    return y

def FPR(x,y):
    F=[0.0, 0.0]
    F[0] = 2*x/y[0]+y[1]+np.exp(x)
    F[1] = y[0]*np.exp(2*x)/(y[1]*2*x)
    return F

def OUT(x,y):
    print("x =",f"{x:.4f}","\ty1 =",f"{y[0]:.4f}","\tu1 =",f"{2*x:.4f}","\tdelta1 =",f"{2*x-y[0]:.4f}","\ty2 =",f"{y[1]:.4f}","\tu2 =",f"{np.exp(x):.4f}","\tdelta2 =",f"{np.exp(x)-y[1]:.4f}")

def printChart(a,b,nx,f1_own,f2_own):

    fig, axs = plt.subplots(1,2)
    x=np.linspace(a,b,nx)
    
    f1_base=2*x
    l1, = axs[0].plot(x,f1_own,'c')
    l2, = axs[0].plot(x,f1_base,'k')
    
    f2_base=np.exp(x)
    l3, = axs[1].plot(x,f2_own,'b')
    l4, = axs[1].plot(x,f2_base,'r')
    
    fig.legend((l1,l2),('Own','2*x'),'upper left')
    fig.legend((l3,l4),('Own','exp(x)'),'upper right')
    plt.tight_layout()
    plt.show()

a=3.0
b=4.0
e=10**-2
nx=10
dMax=100.0
y=[0.0, 0.0]
d=5.0
u=[2*b, np.exp(b)]

while dMax>e:
    y[0]=2*a
    y[1]=np.exp(a)
    y=calculateM5(a,b,nx,2,y,FPR,OUT)
    dMax=0.0
    for i in range(len(y)):
        d=np.abs(u[i]-y[i])
        dMax=max(d,dMax)
    nx*=2
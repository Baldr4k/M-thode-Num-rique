import matplotlib.pyplot as plt
from numpy import *
import time

def hermite(x,X,U,dU):
    i = zeros(len(x),dtype = int)
    for j in range(1,len(X)-1):
        i[X[j]<=x] = j
    s = x-X[i]
    h = ediff1d(X)
    A = ((3*(ediff1d(U))/(h**2))-(dU[1:]+2*dU[:len(X)-1])/h)
    B = (-2*(ediff1d(U))/(h**3)+(dU[:len(X)-1]+dU[1:])/(h**2))
    u_hi = U[i]+s*(dU[i]+s*(A[i]+s*B[i]))
    i+=1
    return u_hi

def hermite_2(x,X,U,dU):
    i = zeros(len(x),dtype = int)
    for j in range(1,len(X)-1):
        i[X[j]<=x] = j
    s = x-X[i]
    h = X[i+1]-X[i]
    t1 = U[i]*(h**3+2*s**3-3*s**2*h)/(h**3)
    t2 = dU[i+1]*((s**2*(s-h)))/(h**2)
    t3 = U[i+1]*(3*h*s**2-2*s**3)/(h**3)
    t4 = dU[i]*(s*(s-h)**2)/(h**2)
    return t1+t2+t3+t4
    

n = 4;
T = arange(0,3*pi/2,3*pi/(2*(n+1)))
T = append(T,[2*pi])
t = linspace(T[0],T[-1],1000)
X = cos(T); Y = sin(T);
dX = -sin(T); dY = cos(T);
plt.plot(X,Y,'.r',markersize=10)
plt.plot(cos(t),sin(t),'--r')
t0 = time.clock()
plt.plot(hermite(t,T,X,dX),hermite(t,T,Y,dY),'-b')
print(time.clock()-t0)
plt.axis("equal"); plt.axis("off")
plt.show()

import matplotlib.pyplot as plt
from numpy import *

def spline2(x,h,U):
    n = len(U); X = arange(0,n+1)*h
    i = zeros(len(x),dtype=int)
    for j in range(1,n):
        i[X[j]<=x] = j
    i = searchsorted(X[1:],x)
    vect = ones(n-1)
    Matrix = (4*eye(n,n)+diag(vect,1)+diag(vect,-1))
    Matrix[0][n-1],Matrix[n-1][0] = 1,1
    Us = append(U[-1],U[:len(U)-1])-2*U[:]+append(U[1:],U[0])
    coef = append(linalg.solve((h**2)/6*Matrix,Us),linalg.solve((h**2)/6*Matrix,Us)[0])
    U=append(U,U[0])
    t1 = coef[i]/(6*h)*(X[i+1]-x)**3
    t2 = coef[i+1]/(6*h)*(x-X[i])**3
    t3 = (U[i]/h - coef[i]*h/6)*(X[i+1]-x)
    t4 = (U[i+1]/h - coef[i+1]*h/6)*(x-X[i])
    return t1 + t2 + t3 + t4


n = 4;
h = 3*pi/(2*(n+1));
T = arange(0,3*pi/2,h)
X = cos(T); Y = sin(T)

fig = plt.figure()
plt.plot(X,Y,'.r',markersize=10)
t = linspace(0,2*pi,100)
plt.plot(cos(t),sin(t),'--r')

t = linspace(0,3*pi/2,100)
print(spline2(t,h,X))
plt.plot(spline2(t,h,X),spline2(t,h,Y),'-b')
plt.axis("equal"); plt.axis("off")
plt.show()
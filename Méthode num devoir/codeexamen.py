from numpy import *

def edpeuler(m,n,beta):
    h = 1/m
    x = arange(0,1+h,h) ; y = arange(0,1+h,h)
    [X,Y] = meshgrid(x,y)
    U = X**2 + Y**2
    for i in range(n):
        U[1:-1,1:-1] += beta*(U[2:,2:] + U[:-2,:-2] - U[2:,:-2] - U[:-2,2:])
    return U

def steffensen(x,tol,nmax,f):
    n = 1
    delta = tol+1
    while (n < nmax and abs(delta>=tol)):
        delta = (f(x)**2)/(f(x+f(x))-f(x))
        x = x - delta
        n += 1
    if delta < tol and n <nmax:
        return x
    else:
        return "nothing was found"
    
def f(x):
    return x**2-2*x+1





    

    
    
    


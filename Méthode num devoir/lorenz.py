from numpy import *

def func(dF):
    return array([10*dF[1] - 10*dF[0], 28*dF[0]-dF[1]-dF[0]*dF[2], dF[0]*dF[1] - 8/3*dF[2]])

def lorenz(Xstart,Xend,Ustart,n):
    U=zeros((n+1,3))
    U[0]=array(Ustart)
    
    h = (Xend - Xstart)/n 
    T = arange(Xstart,Xend+h, h)
    
    for i in range(0,n):
        K1=func(U[i])
        K2=func(U[i]+h/2*K1)
        K3=func(U[i]+h/2*K2)
        K4=func(U[i]+h*K3)
        U[i+1]=U[i]+(h/6)*(K1+2*K2+2*K3+K4)
    
    return T,U

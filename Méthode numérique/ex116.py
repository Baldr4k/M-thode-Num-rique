from scipy.linalg import norm, solve

"""from numpy import *
#Théo
def F(x,U):
    return U[x] + exp(2*x)

def Euler(F,h,U):
    return U[0] + h*F(0,U)

def cheminot(n,h):
    U = zeros(n+1)
    U[0] = 2
    U[1] = Euler(F,h,U)
    for i in range(1,n):
        U[i+1] = 3*((1/3)*(-U[i-1]+4*U[i])+2*h/3*exp(2*(i+1)))
    return U

#prof
def chemi(n,h):
    T = linspace(0,n*h,n+1)
    U = zeros(n+1)
    U[0] = 2
    U[1] = 2 + 3*h
    for i in range(2,n+1):
        U[i] = (-U[i-2] + 4*U[i-1] + 2*h*exp(2*h*(i)))/ (3*(1-2*h/3))
    
    return U

print(cheminot(10,1))
print(chemi(10,1))"""







    
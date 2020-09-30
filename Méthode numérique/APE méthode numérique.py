#3ème exercice
#droite avec deux points
import numpy as np

def f(n,U,t):
    k = int(floor(t))
    if k+2>n:
        k = n-2
    if k-1 < -n:
        k= -n+1
    U_local = U[n+k-1,n+k+3]
    x_i = t-k
    phi = 
    return U_local@phi 
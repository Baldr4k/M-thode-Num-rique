from numpy import *

def diffusion(T,beta,nt):
    for n in range(nt):
       T[1:-1,1:-1]+=beta*(T[2:,1:-1]+T[:-2,1:-1]+T[1:-1,2:]+T[1:-1,:-2]-4*T[1:-1,1:-1])
    return T

def diffusionSmart(T,beta,nt):
    n,m = shape(T)
    S = zeros((n,m))
    for n in range(nt):
        S[:,1:] = T[:,:-1] 
        S[:,0] = T[:,1]
        T[1:-1,:-1] += beta*(T[2:,:-1] + T[:-2,:-1] + T[1:-1,1:] + S[1:-1,:-1] -4*T[1:-1,:-1])
    return T

"""
def diffusionSmart2(T,beta,nt):
    n = 1
    nx, ny = shape(T)
    X = copy(T)
    U = zeros((nx,ny))
    for n in range(nt):
        U[:,1:] = T[:,:-1] 
        U[:,0] = T[:,1]
        for i in range(1, nx-1):
            for j in range(ny-1):
                X[i][j] = T[i][j] + beta*(T[i+1][j]+T[i-1][j]+ T[i][j+1] + U[i][j]-4*T[i][j])
        T = copy(X)
    return T

"""

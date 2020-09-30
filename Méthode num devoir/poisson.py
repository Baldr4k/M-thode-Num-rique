from numpy import*

from scipy.sparse import dok_matrix,eye as speye
from scipy.sparse.linalg import spsolve

def poissonSolve(nCut):
    n=2*nCut+1
    h=2/(n-1)
    A=dok_matrix(speye(n**2),dtype=float64)
    B=zeros(n**2)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if i>nCut or j<nCut:
                index=i+j*n
                A[index,index]=-4
                A[index,index-1],A[index,index+1],A[index,index+n],A[index,index-n] = 1,1,1,1
                B[index]=-h**2
    return spsolve(A.tocsr(),B).reshape(n,n)





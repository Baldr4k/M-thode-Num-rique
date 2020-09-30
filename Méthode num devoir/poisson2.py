from numpy import *
from scipy.sparse.linalg import spsolve
import scipy.sparse as sp


def poissonSolve(nCut):
  n = 2*nCut + 1; m = n*n; h = 2/(n-1) 
  
  A = sp.dok_matrix(sp.eye(m)); B = zeros(m)  
  for i in range(nCut+1,n-1):
    for j in range(1,n-1):
      index = i + j*n
      A[index,index] = 4
      A[index,index-1] = -1
      A[index,index+1] = -1
      A[index,index+n] = -1
      A[index,index-n] = -1
      B[index] = 1
  for i in range(1,nCut+1):
    for j in range(1,nCut):
      index = i + j*n
      A[index,index] = 4
      A[index,index-1] = -1
      A[index,index+1] = -1
      A[index,index+n] = -1
      A[index,index-n] = -1
      B[index] = 1
  return spsolve(A.tocsr()/(h*h),B).reshape(n,n)


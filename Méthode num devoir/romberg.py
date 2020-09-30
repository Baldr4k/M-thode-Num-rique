from numpy import *


def romberg(f,a,b,n,nmax,tol):
    errorEst = tol+1
    I = zeros((int(log2(nmax/n)),int(log2(nmax/n))))
    i = 0 ; length = (b-a)/n
    x = arange(a,b+length, length)
    I[0,0] = trapz(f(x),x)
    while errorEst > tol and 2*n < nmax:
        l = 1 ; i += 1 ; n = n*2
        I2 = I[i-1,i-i]
        old_length = length ; length = length/2
        I[i,i-i] = I2/old_length*length + (length)*sum(f(arange(a+length,b,old_length)))
        while l < i+1:
            I[i,l] = (2**(2*l)*I[i,l-1]-I[i-1,l-1])/(2**(2*l)-1)
            l += 1
        errorEst = abs(I[i,i]-I[i,i-1])
    return I[i,i],n,errorEst
    



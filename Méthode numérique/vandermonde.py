#
# Computing interpolation with Vandermonde matrix
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

#
# -1- Resolution du systeme de Vandermonde
#

from numpy import *
from numpy.linalg import solve

X = array([1,2,3])
U = array([4,5,1])
A = array([X**0,X**1,X**2]).T
a = solve(A,U)
print("Solution du systeme de Vandermonde")
print(array2string(a,formatter={'float_kind':'{0:14.7e}'.format}))
print(array2string(a,formatter={'float_kind':'{0:5.2f}'.format}))
print(a)

#
# -2- Inversion du systeme de Vandermonde
#
#
# Do NOT do that stupid stuff !
# NEVER NEVER NEVER do that, stupid boy !
# On résout un système, on ne l'inverse pas ! (A. Meinguet)
#

from numpy.linalg import inv
A = inv(A)
a = A @ U
print("Inversion de la matrice de Vandermonde")
print(a)

#
# -3- Joli dessin avec mathplotlib
#

from matplotlib import pyplot as plt
#plt.rcParams['figure.facecolor'] = 'silver'
x = linspace(1,3,100)
uh = a[0] + a[1]*x + a[2]*x*x
plt.plot(x,uh,'-b')
plt.plot(X,U,'or')
plt.show()

#
# Idem avec polyval
# Renverse l'ordre du tableau
# On parcourt tout le tableau avec un incrément de -1
#

a = a[::-1] 
x = linspace(1,3,100)
plt.plot(x,polyval(a,x),'-b')
plt.plot(X,U,'or')
plt.show()


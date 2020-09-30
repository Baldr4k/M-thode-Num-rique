#
# good and bad conditioned systems
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *
from numpy.linalg import solve,cond,det,eig

#
# -1- Systeme bien conditionné
#

print("======= Good condition")
A = [[1,1],[1,11]]
b = [2,2]
bpert = [2,2.0001]

x     = solve(A,b)
xpert = solve(A,bpert)
for i in range(len(x)):
  print("   x[%d] = %14.7e and xpert[%d] = %14.7e" % (i,x[i],i,xpert[i]))

lambdas,vect = eig(A)
print("   condition number      = %12.3e" % cond(A))
print("   determinant           = %12.3e" % det(A))
print("   lambda[0]             = %12.3e" % lambdas[0])
print("   lambda[1]             = %12.3e" % lambdas[1])
print("   lambda[0] * lambda[1] = %12.3e" % (lambdas[0]*lambdas[1]))
print("   lambda[1] / lambda[0] = %12.3e" % (lambdas[1]/lambdas[0]))


#
# -2- Systeme mal conditionne
#
#     Ici, on recopie betement le code, c'est exactement ce qu'il ne faudrait pas faire
#     Il faudrait plutot ecrire une fonction avec A et b comme argument....
#     Cette amélioration est laissée au soin du lecteur :-)
#     Comme vous allez le constater, l'enseignant est horriblement paresseux !
#     Plus sérieusement, l'objectif était de garder le code le plus simple possible
#     pour juste illustrer la boite à outil pour l'algebre linaire de numpy
#
#

print("======= Bad condition")
A = [[1,1],[1,1.0001]]
b = [2,2]
bpert = [2,2.0001]

x     = solve(A,b)
xpert = solve(A,bpert)
for i in range(len(x)):
  print("   x[%d] = %14.7e and xpert[%d] = %14.7e" % (i,x[i],i,xpert[i]))

lambdas,vect = eig(A)
print("   condition number      = %12.3e" % cond(A))
print("   determinant           = %12.3e" % det(A))
print("   lambda[0]             = %12.3e" % lambdas[0])
print("   lambda[1]             = %12.3e" % lambdas[1])
print("   lambda[0] * lambda[1] = %12.3e" % (lambdas[0]*lambdas[1]))
print("   lambda[1] / lambda[0] = %12.3e" % (lambdas[1]/lambdas[0]))

# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Probleme 7
#
# Solution detaillee
#  Vincent Legat
#
# -------------------------------------------------------------------------

from numpy import *
from math  import factorial
from numpy.linalg import solve

def doublePrime(alpha):

#
# -1- Calcul des coefficients de la difference finie 
#     On annule tous les termes des developpements en serie de Taylor
#     ... sauf celui qui correspond a u'' : d'ou b(3) = 2
#
#     Exemple pour alpha = [-2 0 2]
#      b_1 + b_2 + b_3      = 0    : annulation terme en u
#     -2/1! b_1 + 2/1! b_3  = 0    : annulation terme en u'
#      4/2! b_1 + 4/2! b_3  = 1    : conserver le terme en u'' :-)

    n = size(alpha);
    A = zeros((n,n));
    for i in range(n):
        A[i,:] = alpha**i
    b = zeros(n)
    b[2] = 2.0 
    beta = solve(A,b)
    
#
# -2- Estimation de l'ordre
#     Si le premier terme de l'erreur est virtuellement nul
#     .... on passe au terme suivant 
#     (cfr ordre bonus des formules symetriques :-)
#
#     Voir la solution de Jérome pour un test un fifrelin plus malin
#     C'est vrai que mon truc est assez empirique et pas très rigoureux 
#

    eps = finfo('float').eps
    if (alpha**n) @ beta >= 10*eps:
        order = n
    else:
        order = n+1;

#
# -3- Calcul du denominateur du terme d'erreur 
#

    factor = factorial(order) / (alpha**order @ beta)
    order = order-2
    
    return beta,factor,order


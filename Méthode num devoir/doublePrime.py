from numpy import *
from math  import factorial
from numpy.linalg import solve
eps = finfo('float').eps

 
def doublePrime(alpha):
    n = len(alpha)
    save = array([alpha])
    unitaire = ones((n,1))
    A = pow(dot(unitaire,save).T, arange(n)).T
    b, b[2] = zeros(n, dtype = int), 2
    beta = solve(A,b)
    print(beta)
    err_machine = (alpha**n) @ beta
    if err_machine >= 10*eps:
        order_of_error = n
    else:
        order_of_error = n+1;
    error = factorial(order_of_error) / (alpha**order_of_error @ beta)
    order_of_error -= 2
    return beta, error, order_of_error
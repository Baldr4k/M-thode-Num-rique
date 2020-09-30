#Question 8
import matplotlib.pyplot as plt
from numpy import *
from scipy.interpolate import CubicSpline

"""
X_k = array([0,1/2, sqrt(3)/2, 1])
U_k = array([1,sqrt(3)/2,1/2,0])
interpol = CubicSpline(X_k,U_k)
x = linspace(0,1,300)
plt.figure()
plt.plot(x,interpol(x))
plt.plot(X_k,U_k,'ob')
plt.show()
"""
#question 9 polynôme de taylor
x = [-1,-1/2,0,1/2,1]
y = cosh(x)
E = (sinh(1)*(2)**5)/120
print(E)

#question 12



from numpy import *
from matplotlib import pyplot as plt


Xstart = 0; Xend = 4; Ustart = 1;
x = linspace(Xstart,Xend,100); u = exp(-5*x)+x
f = lambda x,u : 5*(x-u) + 1

plt.figure()
print(' ==================== Explicit 1st-order Euler ===============');
for j in range(1,5):
  n = pow(2,j+1)
  X = linspace(Xstart,Xend,n+1)
  h = (Xend - Xstart)/n
  U = zeros(n+1); U[0] = Ustart
  for i in range(n):
    U[i+1] = U[i] + h*(5*(X[i]-U[i])+1)
  plt.subplot(2,2,j)
  plt.xlim((-0.1,4.1))
  plt.ylim((-2.0,6.0)); plt.yticks(arange(-2,7,2))
  plt.plot(x,u,'-k',X,U,'.-r',markersize='5.0')
  print(' u(4) = %21.14e (Explicit 1th-order Euler with %2d steps ) ' 
          % (U[-1],n))

plt.figure()
print(' ==================== Implicit 1st-order Euler ===============');
for j in range(1,5):
  n = pow(2,j+1)
  X = linspace(Xstart,Xend,n+1)
  h = (Xend - Xstart)/n
  U = zeros(n+1); U[0] = Ustart
  for i in range(n):
    U[i+1] = (U[i] + h*(5*X[i+1]+1))/(1+5*h)
  plt.subplot(2,2,j)
  plt.xlim((-0.1,4.1))
  plt.ylim((-2.0,6.0)); plt.yticks(arange(-2,7,2))
  plt.plot(x,u,'-k',X,U,'.-g',markersize='5.0')
  print(' u(4) = %21.14e (Implicit 1th-order Euler with %2d steps ) ' 
          % (U[-1],n))



plt.figure()
print(' ==================== Explicit 4th-order Runge Kutta ==========');
for j in range(1,5):
  n = pow(2,j+1)
  X = linspace(Xstart,Xend,n+1)
  h = (Xend - Xstart)/n
  U = zeros(n+1); U[0] = Ustart
  for i in range(n):
    K1 = f(X[i]    ,U[i]       )
    K2 = f(X[i]+h/2,U[i]+K1*h/2)
    K3 = f(X[i]+h/2,U[i]+K2*h/2)
    K4 = f(X[i]+h  ,U[i]+K3*h  )
    U[i+1] = U[i] + h*(K1+2*K2+2*K3+K4)/6
  plt.subplot(2,2,j)
  plt.xlim((-0.1,4.1))
  plt.ylim((-2.0,6.0)); plt.yticks(arange(-2,7,2))
  plt.plot(x,u,'-k',X,U,'.-b',markersize='5.0')
  print(' u(4) = %21.14e (Explicit 4th-order Runge Kutta with %2d steps ) ' 
        % (U[-1],n))
plt.show()

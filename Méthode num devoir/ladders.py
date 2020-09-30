from scipy.linalg import norm, solve

def F(geometry,X):
    x = X[0] ; y = X[1]
    a = geometry[0] ; b = geometry[1] ; c = geometry[2]
    g1 = (b*x)**2 - ((x**2+c**2)*((x+y)**2))
    g2 = (a*y)**2 - ((y**2+c**2)*((x+y)**2))
    
    return [g1,g2]

def dF(geometry,X):
    x = X[0] ; y = X[1]
    a = geometry[0] ; b = geometry[1] ; c = geometry[2]
    dg1_dx = 2*(b**2)*x-(2*(x+y)*(c**2+x*(2*x+y)))
    dg1_dy = -2*(c**2+x**2)*(x+y)
    dg2_dx = -2*(c**2+y**2)*(x+y)
    dg2_dy = 2*(a**2)*y-(2*(x+y)*(c**2+y*(2*y+x)))
    
    return [[dg1_dx,dg1_dy],[dg2_dx,dg2_dy]]
    
def laddersIterate(geometry,X):
    df = dF(geometry,X)
    G = F(geometry,X)
    dx = solve(df,G)
    return X-dx

def laddersSolve(geometry,tol,nmax):
    x_0 = (min(geometry[0],geometry[1]))/2
    x = [x_0,x_0]  
    n = 0; dx = tol+10
    while (norm(dx) > tol and n < nmax):
        dx = solve(dF(geometry,x),F(geometry,x))
        x = x - dx
        n = n+1
        print(" Estimated error %9.2e at iteration %d : " % (norm(dx),n),x)
        
    if x[0]<=tol or x[1]<=tol:
        return[-1,-1]
    else:
        return x
    

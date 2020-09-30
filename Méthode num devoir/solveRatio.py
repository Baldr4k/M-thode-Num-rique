#Théo Denis, 7/02/2019, premier devoir de méthode numérique

def solveRatio(phi) :
    x1 = phi/(2*phi-1)
    x2 = (1-phi)/(1-2*phi)
    x = [x1,x2]
    return x

print(solveRatio(251))




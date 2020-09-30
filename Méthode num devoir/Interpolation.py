#Théo Denis, 17/02/2019, interpolation devoir 2

from numpy import *
from numpy.linalg import solve
import matplotlib.pyplot as plt

n = 4; m = 100
x = (2*pi/(m))*arange(0,m+1)
X = (2*pi/(2*n+1))*arange(0,2*n+1)


##bon maureen c'est la qu'on va s'amuser car y a beaucoup à dire so bare with me
##j'espère que tu as compris le problème, on te demande de faire une interpolation via une somme de fonctions exponentielles multipliées par des coefficients a_k
##pour résoudre le problème il faut trouver ces coéfficients a_k en résolvant un système : U = A*E où U est donné, A est à trouver et E sont les fonctions exponentielles pour X
##tu devras créer aussi des fonctions exponentielles pour x (petit x pas le même qu'avant) car le prof veut que tu lui renvois un tableau uh (qui est l'interpolation de U par les
##abscisses X) pour chaque petit x dans le tableau x.

## si on ramène ça a un cas plus simple, à savoir une interpolation polynomiale de type uh = ax²+bx+c.
## dans cette interpolation tu cherches à trouver les coéfficient (a,b,c) ici ce sont les coéfficients a_k. Tu trouves (a,b,c) à l'aide des équations U=a*X²+b*X+c 
## si jamais tu comprends vraiment pas ça dis le moi et je te ferais un petit cours.

##bon attaquons nous au problème :)
## premièrement il te faut écrire les k allant de -n à n, car ils sont à la base de ta somme. Mais pour ça il te faut trouver n.
## tu sais que ton tableau X est de taille 2n+1 donc n est n = (taille x - 1)/2.
## pour obtenir la taille d'une liste dans python tu fais len(X)

##maintenant que tu as ton n, tu veux créer le vecteur k, ceci ce fait à l'aide de arange(-n,n+1).
## arange fonctionne de cette façon, il te créer un vecteur ligne allant de -n à n+1 non inclus par pas de 1 donc par exemple :
## arange(-2,5) = -2,-1,0,1,2,3,4
## cependant tu vas devoir transformer le type de variable de k en un array (ça te permet d'utiliser des méthodes que tu ne pourrais pas utiliser si c'était pas le cas)
## donc tu écris array(arange(-n,n+1), le .reshape() sert à donner la disposition du vecteur afin de pouvoir faire des multiplications etc plus tard

##deuxièmement, une fois que tu as ton k, tu vas devoir t'amuser à redéfinir les tailles de tes vecteurs X et x en vecteur colonnes comme tu résous un système
## U=A*x et que x est vecteur colonne.
##avec python tu peux appliquer une fonction mathématique sur un vecteur, donc tu peux faire exp(list) si list = [1,2,3] tu auras [exp(1),exp(2),exp(3)]
##c'est pour ça que tu définis kX (qui te sert à l'interpolation) et kx (qui te sert à renvoyer le tableau demandé par le prof plus tard)
## faire la multiplication k*x, tu fais ça à l'aide de X@K le @ est la multiplication matricielle

##le nombre complexe est noté 1j en progra, et donc tu fais tes exponentielles de la somme avec array(exp(1j*kx))
## tu utilises ensuite la fonction solve(X,U) qui te donne le A dans un problème U = A*x, c'est pour ça que a_k = solve(Exp,U)

##finalement tu veux renvoyer les réponses réelles ça se fait avec real(), et comme tu as un problème U=A*E et que tu as maintenant ton A et ton E, tu peux simplement faire
##le produit matricielle entre E@a_k

##c'est un peu compliqué à comprendre et surtout à expliquer par écrit donc si tu as un problème ça me dérange pas de te donner un petit cours :)

def interpolation(X,U,x):
    n = (len(X)-1)//2
    k = array(arange(-n,n+1)).reshape(1,len(X))
    X,x = X.reshape(len(X),1), x.reshape(len(x),1)
    kX,kx = X @ k, x @ k
    Expo_resolution, expo_interpolation = array(exp(1j*kX)), array(exp(1j*kx))
    a_k = solve(Expo_resolution,U)
    return real(expo_interpolation@a_k)


functions = [lambda x : x*(x-2*pi)*exp(-x), 
             lambda x : sin(x)+sin(5*x),
             lambda x : sign(x-2)]
 
for u in functions:
  plt.figure()
  plt.plot(x,u(x),'-b',label='Fonction u')
  U = u(X)
  uh = polyval(polyfit(X,U,len(X)-1),x)
  plt.plot(x,uh,'-g',label='Interpolation polynomiale')
  uh = interpolation(X,U,x)
  plt.plot(x,uh,'-r',label='Interpolation trigonométrique')
  plt.plot(X,U,'ob')
  plt.xlim((-0.2,2*pi+0.2)); plt.ylim((-3,3))
  plt.title('Interpolation trigonométrique : 2n+1 = %d ' % len(X))
  plt.legend(loc='upper right')
  
plt.show() 
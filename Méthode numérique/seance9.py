import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

"""
Auteur : Jerome Eertmans

Notes : complement a la sous-question 5 de l'exercice 102 "Janvier 2011 :
        Schéma symplectique de Bart".

"""

def dist(p1, p2):
    """
    Fonction qui retourne la distance entre deux points.
    """
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return np.sqrt(dx*dx + dy*dy)

def f(x, *args):
    """
    Fonction utilisee par fsolve de scipy afin de resoudre l'equation implicite
    """
    x_old, A, beta, h = args

    # s == 0 si on trouve le bon x (donc U_{i+1})
    s = x_old + h * (beta * A @ x + (1 - beta) * A @ x_old) - x
    return s

# Si False, on utilise la solution analytique de U_{i+1}
# Si True, on utilise la fonction fsolve de scipy pour approcher la solution
# Le second choix est moins rapide et moins robuste / efficace mais calculer la
# solution analytique n'est pas toujours possible :)
use_fsolve = False

def bart(beta, t, x0):
    """
    Applique le schema de Bart au probleme donne pour un vecteur temps.

    Parametres
    ----------
    beta : nombre reel compris entre 0 et 1
        Le parametre du schema de Bart.
        0 - Euleur explicite
        1/2 - Crank-Nicolson
        1 - Euleur implicite
    t : array
        Le vecteur des temps pour lesquels ont souhaite appliquer la methode.
    x0 : array de 2 elements
        Les conditions initiales au probleme telles que x[0] = x0.

    Retourne
    ----------
    x : la solution approchee evaluee aux temps t.

    """
    A = np.array([[0, 1], [-1, 0]])
    x = np.empty((len(t), len(x0)))
    x[0, :] = x0
    for i in range(1, len(t)):
        h = t[i] - t[i-1] # Le pas entre chaque abscisse
        if use_fsolve:
            x[i, :] = fsolve(f, x0=x[i-1, :], args=(x[i-1, :], A, beta, h))

        else:
            # Solution analytique decomposee en plusieurs parties
            C = x[i-1, :] + h*(1-beta)* A@x[i-1, :]
            C1 = C[0]; C2 = C[1]
            a  = h*beta; d = 1 + a*a
            x[i, : ] = [(C1 + a*C2)/d, (C2 - a*C1)/d]

    return x

n = 3 # Nombre de tours
t = np.linspace(0, n*2*np.pi, n*100)
x0 = np.array([1, 0])

_, ax = plt.subplots(1, 3, sharex=True)

# La solution analytique au probleme
true_x, true_y = np.cos(-t), np.sin(-t)

for i, beta in enumerate([0.0, 0.5, 1]):
    x = bart(beta, t, x0)
    ax[i].plot(x[:, 0], x[:, 1], label=(r'$\beta=%.1f$' % beta))
    ax[i].plot(true_x, true_y, color='r', linestyle='--',
                dashes=[1,3], alpha=1, label=r'Solution exacte')
    err = dist(x[-1,:], [true_x[-1], true_y[-1]])
    ax[i].set_title(('Erreur : %.2f' % err))
    ax[i].legend(loc='upper right')
    ax[i].axis('equal')

plt.show()

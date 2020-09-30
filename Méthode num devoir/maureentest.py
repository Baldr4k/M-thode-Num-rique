# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 19-20
# Problème 1
#
# Script de test
#  
# Vincent Legat
#
# -------------------------------------------------------------------------
# 
 
from maureen import diophantine
 
#
# -1- Test de la fonction diophantine : on calcule la solution de l'équation x**a + y**b = z**c
#     dont la somme des carrés est la plus proche de 1800
#     On effectue la recherche pour tous les entiers compris entre 0 et 30 :-)
#
 
a = 2; b = 3; c = 4
n = 30
norm = 800
x = diophantine(a,b,c,n,norm)
 
print("==== Computing the solution of the diophantine equation :") 
print(" === [a,b,c] = [%d,%d,%d] n = %d norm = %d " % (a,b,c,n,norm))
print(" === Solution is ",x)
 
#
# -2- Le plus grand triangle rectangle de côtés entiers de longueur inférieure ou égale à 20 :-)
#
#
 
x = diophantine(2,2,2,20,200)
print("final answer : " + str(x))
 
from matplotlib import pyplot as plt
 
plt.rcParams['toolbar'] = 'None'
plt.rcParams['figure.facecolor'] = 'moccasin'
plt.figure("Diophantine equations :-)")
plt.axis('equal')
plt.axis('off')
plt.text(x[0]/2  ,-0.5  ,'x = %d'%x[0],weight='bold',color='red')
plt.text(x[0]+0.5,x[1]/2,'y = %d'%x[1],weight='bold',color='red')
plt.text(x[0]/4  ,x[1]/2,'z = %d'%x[2],weight='bold',color='red')  
plt.text(-1       ,x[1]  ,'%d = %d + %d = %d*%d + %d*%d = %d*%d = %d'%
         (x[0]*x[0]+x[1]*x[1],x[0]*x[0],x[1]*x[1],x[0],x[0],x[1],x[1],x[2],x[2],x[2]*x[2]),weight='bold',color='red')  
plt.fill([0,x[0],x[0],0],[0,0,x[1],0],'-b')
plt.show()
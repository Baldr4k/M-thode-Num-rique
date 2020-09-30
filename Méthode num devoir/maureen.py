# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 19-20
# Problème 1
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'INSTRUCTION import / from :-)
# UTILISER UNIQUEMENT PYTHON SANS AUCUN PACKAGE !
 
def diophantine(a,b,c,n,norm) :
    sol = "toujours pas de sol"
    
    #afin de tester toutes les combinaisons de chiffre
    for x in range(1,n+1):
        for y in range(1,n+1):
            for z in range(1,n+1):
                
                #on regarde si x, y et z vérifie l'équation
                if (x**a+y**b==z**c):
                    
                    #si sol n'a pas encore eu de valeur alors on lui en donne une
                    if (sol=="toujours pas de sol"):
                        sol = [x,y,z]
                        
                    #on vérifie si la nouvelle solution donnée par [x,y,z] est plus proche de norme que sol    
                    if (abs(norm - (x**2+y**2+z**2)) <= abs(norm - (sol[0]**2+sol[1]**2+sol[2]**2))):
                        
                        #si x est plus grand que le x de la solution alors on change
                        if x>sol[0]:
                            sol = [x,y,z]
    return sol

#j'espère que tu as compris :) sinon hésite pas à envoyer un mensenger,



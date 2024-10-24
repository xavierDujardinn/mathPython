import random as rm
import elemSuite as suite
import math

def img(x):
    return math.sin(x)

def monteCarlo(C=1.1, c=0, a=0, b=math.pi):
    nbPointsMax = 10000
    nbPointsTot = 0
    nbPointsVal = 0
    estComptabilise = True

    a1 = 1664525      # multiplicateur
    c1 = 1013904223   # incrément
    m = 2**32        # module
    uk = 123456789  # seed initial uk
    vk = 123465789 # seed initial vk
    while nbPointsTot < nbPointsMax:

        uk = suite.elemSuite(uk, a1, c1, m)
        vk = suite.elemSuite(vk, a1, c1, m)

        # on divise par m afin d'avoir un chiffre qui appartient [0,1]
        xk = a + (b-a) * (uk / m)
        yk = c + (C-c) * (vk / m)

        fxk = img(xk)

        if yk < fxk :
            # On comptabilise le point
            nbPointsVal += 1
        elif yk == fxk :
            #On comptabilise le point 1 fois sur 2
            if estComptabilise :
                nbPointsVal += 1
            estComptabilise = not estComptabilise

        nbPointsTot += 1

    proportion = nbPointsVal/ nbPointsTot
    print("Proportion : ",proportion)

    resultat = (b-a)*c + (C-c)*(b-a)*proportion
    print("Resultat : ",resultat)
from validite.utils import khiTable as khi
from validite.utils.lastCol import last_col
from validite.utils.showTab import show_tab

# Fonction de tests des sauts
# valeur : variable qui donne la valeur des modalités testée [0,9]
def testSauts(yn, valeur = 0):

    # On ne garde que les 100 premières valeurs
    yn = yn[:100]

    # Modalités et répetitions
    modalite = [i for i in range(len(yn) - 1)]

    ri = [0 for _ in range(len(modalite))]
    for i in range(len(yn)):
        if yn[i] == valeur and i <= len(yn) - 1:
            if valeur in yn[i+1:]:
                ri[yn[i + 1:].index(valeur)] += 1

    # Probabilités et fréquences théoriques
    pi = [pow(0.9,i)*0.1 for i in range(len(modalite))]
    nPi = [len(yn) * Pi for Pi in pi]

    lastCol = [last_col(ri[i], nPi[i]) for i in range(len(modalite))]

    # On affiche le tableau
    show_tab(modalite, ri, pi, nPi, lastCol)

    # Vérification si regroupements nécessaire
    if any(valeur < 5 for valeur in nPi):
        print("\nRegroupement nécessaire...\n")
        for i in range(len(nPi) -1, -1, -1):
            if i - 1 >= 0:
                if nPi[i] < 5:
                    nPi[i-1] += nPi[i]
                    nPi.pop(i)

                    pi[i-1] += pi[i]
                    pi.pop(i)

                    lastCol[i-1] += lastCol[i]
                    lastCol.pop(i)

                    ri[i-1] += ri[i]
                    ri.pop(i)

                    modalite.pop(i)

        # les x1 seront incohérents sur les classes regroupées mais trkl y a pire dans la vie
        show_tab(modalite, ri, pi, nPi, lastCol)

        # Calcul final
        khiObservable = sum(lastCol)
        v = len(modalite) - 1

        print(f"Khi observable : {khiObservable} , degré de liberté : {v}")
        print(f"{khiObservable} <= ? {khi.getKhiSqVal(v)}]")
        return ("==> on ne rejette pas" if khiObservable <= khi.getKhiSqVal(v) else "on rejette") + " l'hypothèse"




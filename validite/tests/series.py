from validite.utils import khiTable as khi
from validite.utils.lastCol import last_col
from validite.utils.showTab import show_tab

# Fonction de tests des séries
def testSeries(yn):
    # On prend que 500 valeurs pour ne pas faire de regroupements
    yn = yn[:500]

    # setup des modalités du test
    modalite = []
    for i in range(10):
        for j in range(10):
            modalite.append((i,j))

    print(modalite)

    pi = [0.01 for _ in range(len(modalite))]

    # La fréquence d'apparition de chaque valeur
    ri = [0 for _ in range(len(modalite))]
    for i in range(len(yn)):
        if i + 1 < len(modalite):
           ri[modalite.index((yn[i],yn[i+1]))] += 1

    # Frequence theorique
    nPi = [len(yn) * Pi for Pi in pi]

    lastCol = [last_col(ri[i], nPi[i]) for i in range(len(modalite))]

    # On affiche le tableau
    show_tab(modalite, ri, pi, nPi, lastCol)

    # Calcul final
    khiObservable = sum(lastCol)
    v = len(modalite) - 1

    print(f"Khi observable : {khiObservable} , degré de liberté : {v}")
    print(f"{khiObservable} <= ? {khi.getKhiSqVal(v)}]")
    return ("==> on ne rejette pas" if khiObservable <= khi.getKhiSqVal(v) else "on rejette") + " l'hypothèse"



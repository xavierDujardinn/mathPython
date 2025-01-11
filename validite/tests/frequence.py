from validite.utils import khiTable as khi
from validite.utils.lastCol import last_col
from validite.utils.showTab import show_tab

# Fonction de test des fréquences
def testFrequence(YN):

    # modalités de 0 à 9
    modalite = [i for i in range(10)]
    pi = [0.1 for _ in range(len(modalite))]

    # La fréquence d'apparition de chaque valeur
    ri = [YN.count(val) for val in modalite]

    # Frequence theorique
    nPi = [len(YN) * Pi for Pi in pi]

    lastCol = [last_col(ri[i], nPi[i]) for i in range(len(modalite))]

    # On affiche le tableau
    show_tab(modalite, ri, pi, nPi, lastCol)

    # Calcul final
    khiObservable = sum(lastCol)
    v = len(modalite) - 1

    print(f"Khi observable : {khiObservable} , degré de liberté : {v}")
    print(f"{khiObservable} <= ? {khi.getKhiSqVal(v)}]")
    return ("==> on ne rejette pas" if khiObservable <= khi.getKhiSqVal(v) else "on rejette") + " l'hypothèse"

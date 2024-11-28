from numpy.distutils.system_info import x11_info
import elemSuite as eS
import math

def filtre(tab, ri):
    newTab = []
    newTab2 = []
    for i in range(len(tab)-1):
        if tab[i] >= 5:
            newTab.append(tab[i])
            newTab2.append(ri[i])
        else:
            if newTab[len(newTab)-1] < 5:
                newTab[len(newTab)-1] = newTab[len(newTab)-1] + tab[i]
                newTab2[len(newTab2)-1] = newTab2[len(newTab2)-1] + ri[i]
            else:
                newTab.append(tab[i])
                newTab2.append(ri[i])
    if newTab[len(newTab)-1] < 5:
        newTab[len(newTab)-2] = newTab[len(newTab)-2] + newTab[len(newTab)-1]
        newTab2[len(newTab2)-2] = newTab2[len(newTab2)-2] + newTab2[len(newTab2)-1]
        newTab2.pop(len(newTab2)-1)
        newTab.pop(len(newTab)-1)
    print(newTab, newTab2)
    return newTab, newTab2

def getKhiSqVal(v):
    khiTable = [
        3.841,
        5.991,
        7.815,
        9.488,
        11.070,
        12.592,
        14.067,
        15.507,
        16.919,
        18.307,
        19.675,
        21.026,
        22.362,
        23.685,
        24.996,
        26.296,
        27.587,
        28.869,
        30.144,
        31.410,
        32.671,
        33.924,
        35.172,
        36.415,
        37.652,
        38.885,
        40.113,
        41.337,
        42.557,
        43.773
    ]
    return khiTable[v-1]


def base():
    # On définis simplement la base des test
    x0 = 7
    a = 5
    c = 3
    m = 16

    n = 1000

    suite = [x0]

    x = x0
    y = 0
    i = 0
    while (i < n):
        y = eS.elemSuite(x,a,c,m)
        suite.append(y)
        x = y
        i += 1

    print(f"Suite : {suite} \nTaille : {len(suite)}")

    un = [xn/m for xn in suite]
    yn = [int(Un * 10) for Un in un]

    print(f"Un : {un}")
    print(f"Yn : {yn}")
    return un, yn, suite

def last_col (ri, niPi):
    # fonction pour le cacul redondant de la dernière colone
    return pow(ri - niPi, 2) / niPi

def show_tab(xi, ri, pi, nPi, lastCol):
    # fonction pour afficher le tableau
    print("Xi\t|Ri\t|Pi\t|N*Pi\t|(Ri-NPi)²/(NPi)")
    for i in range(len(lastCol)):
        print(f"{xi[i]}\t|{ri[i]}\t|{pi[i]}\t|{nPi[i]}\t|{lastCol[i]}")

def testFrequence(yn):
    modalite = [i for i in range(10)]
    ri = [yn.count(val) for val in modalite]
    pi = [0.1 for _ in range(len(modalite))]
    nPi = [len(yn) * Pi for Pi in pi]
    lastCol = [last_col(ri[i], nPi[i]) for i in range(len(modalite))]
    show_tab(modalite, ri, pi, nPi, lastCol)
    khiObservable = sum(lastCol)
    v = len(modalite) - 1
    print(f"Khi observable : {khiObservable} , degré de liberté : {v}")
    print(f"{khiObservable} <= ? {getKhiSqVal(v)}]")
    return "on ne rejette pas" if khiObservable <= getKhiSqVal(v) else "on rejette"

def testSauts(yn, valeur=0):
    yn = yn[:100]
    print(yn)
    modalite = [i for i in range(len(yn) - 1)]
    ri = [0 for _ in range(len(modalite))]

    for i in range(len(yn)):
        if yn[i] == valeur and i <= len(yn) - 1:
            if valeur in yn[i+1:]:
                ri[yn[i + 1:].index(valeur)] += 1
    pi = [pow(0.9,i)*0.1 for i in range(len(modalite))]
    nPi = [len(yn) * Pi for Pi in pi]



    newNpi, newRi = filtre(nPi, ri)

    newMod = [0 for i in range(len(newNpi))]
    newPi = [0 for i in range(len(newNpi))]

    lastCol = [last_col(newRi[i], newNpi[i]) for i in range(len(newNpi)-1)]
    print(len(newNpi) , len(newRi))

    show_tab(newMod, newRi, newPi, newNpi, lastCol)
    khiObservable = sum(lastCol)
    v = len(newNpi) - 1
    print(f"Khi observable : {khiObservable} , degré de liberté : {v}")
    print(f"{khiObservable} <= ? {getKhiSqVal(v)}]")
    return "on ne rejette pas" if khiObservable <= getKhiSqVal(v) else "on rejette"
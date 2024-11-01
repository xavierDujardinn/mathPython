import elemSuite as eS


def base():
    # On définis simplement la base des test
    x0 = 19
    a = 61
    c = 49
    m = 120

    suite = [x0]

    x = x0
    y = 0
    while (y != x0):
        y = eS.elemSuite(x,a,c,m)
        if (y != x0):
            suite.append(y)
            x = y

    print(f"Suite : {suite} \nTaille : {len(suite)}")

    un = [xn/m for xn in suite]
    yn = [int(Un * 10) for Un in un]

    print(f"Un : {un}")
    print(f"Yn : {yn}")
    return un, yn, suite

def last_col (ri, niPi):
    # fonction pour le cacul redondant de la dernière colone
    return ((ri - niPi)**2) / niPi

def show_tab(xi, ri, pi, nPi, lastCol):
    # fonction pour afficher le tableau
    print("Xi\tRi\tPi\tN*Pi\t(Ri*NPi)²/(NPi)")
    for i in range(len(xi)):
        print(f"{xi[i]}\t{ri[i]}\t{pi[i]}\t{nPi[i]}\t{lastCol[i]}")

def testFrequence(yn, suite):
    modalite = [i for i in range(10)]
    ri = [yn.count(val) for val in modalite]
    pi = [0.1 for _ in range(len(modalite))]
    nPi = [len(yn) * Pi for Pi in pi]
    lastCol = [last_col(ri[i], nPi[i]) for i in range(len(modalite))]
    show_tab(modalite, ri, pi, nPi, lastCol)
    khiObservable = sum(lastCol)
    v = len(modalite) - 1
    print(f"Khi observable : {khiObservable} , degré de liberté : {v}")


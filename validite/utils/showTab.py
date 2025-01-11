# fonction pour afficher le tableau
def show_tab(xi, ri, pi, nPi, lastCol):
    print("Xi\t|Ri\t|Pi\t|N*Pi\t|(Ri-NPi)²/(NPi)")
    for i in range(len(lastCol)):
        print(f"{xi[i]}\t|{ri[i]}\t|{pi[i]}\t|{nPi[i]}\t|{lastCol[i]}")


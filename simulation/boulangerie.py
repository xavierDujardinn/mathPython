from utils.elemSuite import elemSuite

# forcer le hasard de la categorie
def genererCategorie(x0,a,c,m):
    x1 = elemSuite(x0,a,c, m)
    u1 = x1 / m

    if u1 < 0.30:
        categorie = "élevée"
    elif u1 < 0.75:
        categorie = "moyenne"
    else:
        categorie = "basse"

    x0 = x1
    return x0, categorie

# forcer le hasard de la demande
def genererDemande(x0,a,c,m, categorie):
    x1 = elemSuite(x0,a,c, m)
    u1 = x1 / m

    if categorie == "élevée":
        if u1 < 0.05:
            demande = 36
        elif u1 < 0.15:
            demande = 48
        elif u1 < 0.4:
            demande = 60
        elif u1 < 0.72:
            demande = 72
        elif u1 < 0.9:
            demande = 84
        else:
            demande = 96

    elif categorie == "moyenne":
        if u1 < 0.1:
            demande = 36
        elif u1 < 0.3:
            demande = 48
        elif u1 < 0.6:
            demande = 60
        elif u1 < 0.85:
            demande = 72
        elif u1 < 0.95:
            demande = 84
        else:
            demande = 96

    else:
        if u1 < 0.15:
            demande = 36
        elif u1 < 0.4:
            demande = 48
        elif u1 < 0.75:
            demande = 60
        elif u1 < 0.9:
            demande = 72
        elif u1 < 0.95:
            demande = 84
        else:
            demande = 96

    x0 = x1
    return x0, demande


# chapitre 7.3 module 1
def simulation(x0, a, c, m, dureeSimulation = 10):
    print ("#######################\nDebut Simulation Boulangerie\n#######################\n")
    nbBriochesOptimal = -1
    beneficeMax = 0
    nbBrioches = 36
    while nbBrioches <= 96:
        benefice = 0
        t = 1
        while t <= dureeSimulation:
            x0, categorie = genererCategorie(x0,a,c,m)
            x0, demande = genererDemande(x0,a,c,m,categorie)

            if demande <= nbBrioches:
                ciffreAffaires = demande * 0.4 + (nbBrioches - demande) * 0.1
            else:
                ciffreAffaires = demande * 0.4 - (demande - nbBrioches) * 0.15

            benefice += ciffreAffaires - nbBrioches * 0.25
            t += 1

        if benefice > beneficeMax:
            beneficeMax = benefice
            nbBriochesOptimal = nbBrioches

        print(f"Nombre de brioches : {nbBrioches}, bénéfice : {benefice}")
        nbBrioches += 12


    print(f"\nLe nombre de brioches optimal est {nbBriochesOptimal} pour un bénéfice de {beneficeMax}\n")

    return nbBriochesOptimal, beneficeMax


simulation(0,31415821,1,10**8)
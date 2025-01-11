from utils import elemSuite as ES
# Mise en place de la suite pour les tests source des valeurs : chatGPT
def setup():
    x0 = 0
    a = 31415821
    c = 1
    m = 10**8
    XN, UN, YN = ES.createSuite(x0, a, c, m)
    return XN, UN, YN

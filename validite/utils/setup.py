from utils import elemSuite as ES
# Mise en place de la suite pour les tests source des valeurs : chatGPT
def setup():
    x0 = 123456
    a = 1664525
    c = 1013904223
    m = 2**32
    XN, UN, YN = ES.createSuite(x0, a, c, m)
    return XN, UN, YN

from validite.tests.frequence import testFrequence
from validite.tests.sauts import testSauts
from validite.tests.series import testSeries
from validite.utils.setup import setup

print ("###################\nValeurs\n###################\n")

# setup de l'environnement
XN, UN, YN = setup()

print ("###################\nTest des Fréquences\n###################\n")

print(testFrequence(YN) + "\n")

print ("###################\nTest des Sauts\n###################\n")

print(testSauts(YN) + "\n")

print ("###################\nTest des Séries\n###################\n")

print(testSeries(YN) + "\n")
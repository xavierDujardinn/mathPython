import elemSuite
import monteCarlo as mc
import tests


# mc.monteCarlo()
base = tests.base()
xn = base[0]
yn = base[1]
suite = base[2]

tests.testFrequence(yn, suite)
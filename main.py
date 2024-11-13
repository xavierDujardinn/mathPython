import elemSuite
import monteCarlo as mc
import tests


# mc.monteCarlo()
base = tests.base()
xn = base[0]
yn = base[1]
suite = base[2]

print(tests.testFrequence(yn))
print("----------------------")
print(tests.testSauts(yn, 0))
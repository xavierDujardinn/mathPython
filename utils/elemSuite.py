def elemSuite (xn,a,c,m):
    return (a*xn + c) % m

def createSuite(x0, a, c, m, nbValues = 1000, d=10):
    XN = []
    for i in range(nbValues-1):
        x1 = (a*x0 + c) % m
        XN.append(x1)
        x0 = x1
    UN = [i/m for i in XN]
    YN = [int(i*d) for i in UN]
    print(f"XN : {XN}\n-----")
    print(f"UN : {UN}\n-----")
    print(f"YN : {YN}\n-----")
    return XN, UN, YN



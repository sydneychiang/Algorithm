


def integerMultiplication(r, s):
    print(str(r))
    n = len(str(r))
    print(n)
    # rLst = [int(str(r)[0:n/2]), int(str(r)[n/2:len(str(r))])]
    # sLst = [int(str(s)[0:n/2]), int(str(s)[n/2:len(str(s))])]
    rLst = []
    sLst = []


    # rEquation = rLst[0] * pow(10, n/2) + rLst[1]
    # sEquation = sLst[0] * pow(10, n/2) + sLst[1]

    z = (rLst[0] * sLst[0]) * pow(10, n) + (rLst[0] * sLst[1] + rLst[1] * sLst[0]) * pow(10, n/2) + (rLst[1] * sLst[1])
    return z

def improvedIntegerMultiplication(r, s):
    n = len(str(r))
    rLst = [int(str(r)[0:n / 2]), int(str(r)[n / 2:len(str(r))])]
    sLst = [int(str(s)[0:n / 2]), int(str(s)[n / 2:len(str(s))])]

    # rEquation = rLst[0] * pow(10, n/2) + rLst[1]
    # sEquation = sLst[0] * pow(10, n/2) + sLst[1]

    u = (rLst[0] + rLst[1]) * (sLst[0] + sLst[1])
    v = rLst[0] * sLst[0]
    w = rLst[1] * sLst[1]

    z = v * pow(10,n) + (u-v-w) * pow(10, n/2) + w
    return z



print(improvedIntegerMultiplication(3467, 5923))
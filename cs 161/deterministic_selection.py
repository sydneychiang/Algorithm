import math

def bruteForceSelect(S, k):
    S.sort()
    return S[k-1]

def createGroup(S):
    outer_i = math.ceil(len(S)/5)
    return [S[i*5:i*5+5] for i in range(outer_i)]


def createGroupMedian(group):
    medianlst = []
    for lst in group:
        lst.sort()
        medianlst.append(lst[math.ceil(len(lst)/2)])
    return medianlst

def DSelect(S, k):
    n = len(S)
    if n <= 5:
        return bruteForceSelect(S,k)

    group = createGroup(S)
    groupMedian = createGroupMedian(group)

    m = DSelect(groupMedian, math.ceil(math.ceil(n/5)/2))
    L, E, G = [], [], []

    for s in S:
        if s < m:
            L += [s]
        elif s == m:
            E += [s]
        else:
            G += [s]

    if len(L) >= k:
        return DSelect(L, k)
    elif len(L) + len(E) >= k:
        return m
    else:
        return DSelect(G, k - len(L) - len(E))


#############################INPUT########################################
S = [29,90,93,14,11,38,22,81,91,17,62,83,97,64,66,26,55,89,
     51,24,32,78,66,47,61,76,82,70,85,73,15,99,86,13,88]
k = 18
#############################INPUT########################################


kthSmallest = DSelect(S, k)
print(f"{k}th smallest integer of S:", kthSmallest)
# print(sorted(S), sorted(S)[k-1])
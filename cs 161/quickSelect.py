import random

'''
splitList()
possible str vals:
L - all elements in S less than m
E - all elements in S equal to m
G - all elements in S greater than m
'''
def splitList(S, m, str):
    if str == "L":
        return [element for element in S if element < m]
    elif str == "E":
        return [element for element in S if element == m]
    elif str == "G":
        return [element for element in S if element > m]



'''
quickSelect(S, k)
returns the kth smallest item from the sequence S

worst-case running time: theta(n^2)
expected running time is O(n)
'''
def quickSelect(S, k):
    if len(S) == 1:
        return S[0]
    m = S[random.randint(0, len(S)-1)]
    # m = 37
    L = splitList(S, m, "L")
    E = splitList(S, m, "E")
    G = splitList(S, m, "G")

    print(L, E, G)
    if len(L) >= k:
        return quickSelect(L, k)
    elif len(L) + len(E) >= k:
        return m
    else:
        print(k - len(L) - len(E))
        return quickSelect(G, k - len(L) - len(E))



#############################INPUT########################################
# S = [9,5,1,1,2,3,7,8,9]
S = [53,28,77,21,13,84,41,69,26,36,37,54]
#############################INPUT########################################


kthSmallest = quickSelect(S, 8)
print("kth smallest integer of S:", kthSmallest)
import math


######################################INPUT############################################
# data = [[1, 'A', 0.26], [2, 'B', 0.06], [3, 'C', 0.24], [4, 'D', 0.04], [5, 'E', 0.16], [6, 'F', 0.10], [7, 'G', 0.14]]
# data = [[1, 'A', 17], [2, 'B', 12], [3, 'C', 23], [4, 'D', 10], [5, 'E', 31]]
data = [[1, 'A', 0.11], [2, 'B', 0.12], [3, 'C', 0.06], [4, 'D', 0.22], [5, 'E', 0.05], [6, 'F', 0.03], [7, 'G', 0.41]]
######################################INPUT############################################



n = len(data)+1
W = [['N' for i in range(len(data)+1)] for i in range(len(data)+1)]
E = [['N' for i in range(len(data)+1)] for i in range(len(data)+1)]
root = [['N' for i in range(len(data)+1)] for i in range(len(data)+1)]


p = [i[2] for i in data]


def OptimalTreeCost(p):
    for i in range(1, n+1):
        E[i-1][i-1] = 0
        W[i-1][i-1] = 0
    for size in range(1, n+1):
        for i in range(1, n-size+1):
            j = i + size - 1
            E[i-1][j] = math.inf
            W[i-1][j] = W[i-1][j-1] + p[j-1]
            for r in range(i, j+1):
                x = E[i-1][r-1] + E[r][j] + W[i-1][j]
                if x < E[i-1][j]:
                    E[i-1][j] = round(x, 2)
                    root[i-1][j] = r
    return E, root
            



def formatMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end='\t')
        print()


temp = OptimalTreeCost(p)

formatMatrix(temp[0])
print('------------------------')
formatMatrix(temp[1])


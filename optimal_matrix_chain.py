import math
def optMatrixChain(d):
    
    for i in range(1, len(d)):
        M[i][i] = 0
    for len1 in range(2, len(d)):
        for i in range(1, len(d) - len1 + 1):
            j = i + len1 - 1
            M[i][j] = math.inf
            for k in range(i, j):
                x = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
                if x < M[i][j]:
                    M[i][j] = x
                    S[i][j] = k

    
    return M, S








def formatMatrix(M):
    for i in range(1,len(M)):
        for j in range(1,len(M[i])):
            print(M[i][j], end='\t')
        print()

# d = [10, 7, 12, 6, 8, 13, 9]
d = [31, 42, 20, 46, 18, 49, 24]
M = [["N" for i in range(len(d))] for i in range(len(d))]
S = [["N" for i in range(len(d))] for i in range(len(d))]

out = optMatrixChain(d)
formatMatrix(out[0])
print("--------------------------------------------------------")
formatMatrix(out[1])





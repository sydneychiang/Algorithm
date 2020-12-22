
def compute_opt_strategy(w,v):
    for i in range(len(v)+1): 
        OPT[i][0] = 0
    for j in range(W+1):
        OPT[0][j] = 0
    for i in range(1, len(v)+1):
        for j in range(1, W+1):
            if (w[i-1] > j) or (v[i-1] + OPT[i-1][j-w[i-1]] <= OPT[i-1][j]):
                OPT[i][j] = OPT[i-1][j]
                keep[i][j] = False
            else:
                OPT[i][j] = v[i-1] + OPT[i-1][j-w[i-1]]
                keep[i][j] = True
    return OPT, keep


def print_solution(OPT, keep, i, j):
    if i ==0: 
        return
    if keep[i][j]:
        print_solution(OPT, keep, i-1, j-w[i-1])
        print(i)
    else:
        print_solution(OPT, keep, i-1, j)




def formatMatrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end='\t')
        print()



#############################INPUT########################################
W = 15
w = [5, 9, 2, 7, 8, 3]
v = [7, 12, 14, 11, 15, 5]
#############################INPUT########################################


OPT = [["N" for i in range(W+1)] for i in range(len(v)+1)]
keep = [["N" for i in range(W+1)] for i in range(len(v)+1)]

out = compute_opt_strategy(w,v)
formatMatrix(out[0])
print("--------------------------------------------------------")
formatMatrix(out[1])
print()
print('KEEP')
print_solution(out[0], out[1], len(w), W)


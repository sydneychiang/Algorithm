# Weighted Interval Scheduling
################################################################

# Setup
#######################################################
# intervals = [[1,3,2], [2,6,4], [5,7,4], [4,10,7], [8,11,2], [9,12,1]]
intervals = [[1,2,6],[3,4,3],[4,6,4],[3,8,8],[8,10,1],[2,12,8]]

# intervals = [[1,2,5], [1,3,4], [2,4,7], [3,5,2], [1,6,3], [4,7,5], [6,8,7], [7,9,4]]

def s(j):
    return intervals[j-1][0]

def f(j):
    return intervals[j-1][1]

def v(j):
    return intervals[j-1][2]

def p(j):
    return intervals[j-1][3]

# Add the p(j) column
for i in range(len(intervals)):
    j = i
    while j >= 0:
        if s(i+1) >= f(j+1):
            intervals[i].append(j+1)
            break
        j-=1
    if j == -1:
        intervals[i].append(0)


# sort by finish time
intervals.sort(key=lambda x: x[1])



# Algorithms
########################################################
# Recursive
def OPT_Recursive(j):
    if j ==0:
        return 0
    else:
        return max(v(j)+OPT_Recursive(p(j)), OPT_Recursive(j-1))

# Memoized recursion
def OPT_Memoized_Recursive(j):
    if j == 0:
        return 0
    else:
        if M[j] == None:
            M[j] = max(v(j) + OPT_Memoized_Recursive(p(j)), OPT_Memoized_Recursive(j-1))
        return M[j]

# Dynamic Programming
def OPT_Dynamic_Programming():
    M[0] = 0
    for j in range(1, len(intervals)+1):
        M[j] = max(v(j) + M[p(j)], M[j-1])
    return M[-1]

# Compute Optimal Set of Intervals With Dynamic Programming Algorithm

def OPT_Dynamic_Programming_Intervals():
    M[0] = 0
    for j in range(1, len(intervals)+1):
        if v(j) + M[p(j)] > M[j-1]:
            M[j] = v(j) + M[p(j)]
            keep[j] = True
        else:
            M[j] = M[j-1]
            keep[j] = False

def Print_Solution(j):
    if j == 0:
        return
    if keep[j]:
        Print_Solution(p(j))
        print(j)
    else:
        Print_Solution(j-1)



# Function Calls
#################################################
M = [None] * (len(intervals) + 1)
print(OPT_Recursive(len(intervals)))


M = [None] * (len(intervals) + 1)
print(OPT_Memoized_Recursive(len(intervals)))


M = [None] * (len(intervals) + 1)
print(OPT_Dynamic_Programming())


print('INTERVALS:')
M = [None] * (len(intervals) + 1)
keep = [None] * (len(intervals) + 1)
OPT_Dynamic_Programming_Intervals()
Print_Solution(len(intervals))
print(keep)
print(M)
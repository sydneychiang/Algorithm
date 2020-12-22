import math;


# Fractional knapsack
# Running time: O(n log n)
# Storage: O(n)
# A - list
# cap - Knapsack capacity
def fractionalKnapsack(A, cap):
    densities = []
    for pair in A:
        densities.append((pair[1] / pair[0], pair))
    densities.sort(key=lambda x: x[0], reverse=True)
    # print('SORTED [Density, (weight, value)]: \n   ', densities)


    currentIndex = 0
    total = 0
    while cap > 0:
        if densities[currentIndex][1][0] <= cap:
            total += densities[currentIndex][1][1]
            cap -= densities[currentIndex][1][0]
        else:
            total += (cap / densities[currentIndex][1][0]) * densities[currentIndex][1][1]
            break
        currentIndex += 1
    # print('TOTAL WEIGHT: \n   ', total)
    # print()
    #
    #
    # print(' %9s |%6s |%6s |%6s' % ("Obj", "Weight", "Value", "Value Density"))
    # print('--------------------------------------')
    # for tuple in densities:
    #     print(' %9s |%6s |%6s |%6s' % (tuple[1], tuple[1][0], tuple[1][1], tuple[0]))


fractionalKnapsack([(20, 100), (24, 24), (10, 20), (16, 48), (18, 72)], 50)

def compute_opt_strategy(w, v):
    for i in range(0, len(v)):
        OPT[i][0] = 0
    for j in range(0, len(w)):
        OPT[0][j] = 0
    for i in range(1, len(v)):
        for j in range(1, len(w)):
            if (w[i] > j) or (v[i] + OPT[i-1][j-w[i]] <= OPT[i-1][j]):
                OPT[i][j] = OPT[i-1][j]
                keep[i][j] = False
            else:
                OPT[i][j] = v[i] + OPT[i-1][j-w[i]]
                keep[i][j] = True
    return (OPT, keep)

def print_solution(OPT, keep, i, j):
    if keep[i][j]:
        print_solution(OPT, keep, i-1, j-w[i])
        print(i)
    else:
        print_solution(OPT, keep, i-1, j)

# OPT = [[],[]]
# keep = []

w = [20, 90]
v = [80, 90]
# (OPT, keep) = compute_opt_strategy(w,v)
# print(OPT)
# print_solution(OPT, keep, n, w)

# Huffman Coding in python
# Running time: O(nlogn)
#     time breakdown: using a heap to store the weight of each tree O(log n), takes O(n) iterations, one per item

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

#INPUT STRING CHANGE THIS TO CHANGE INPUT
# string = 'BCAADDDCCACACAC'
string = ""
string += "A" * 16
string += "B" * 8
string += "C" * 21
string += "D" * 5
string += "E" * 28
string += "F" * 7
string += "G" * 15
print(string)


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
# print()
# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))




def mergeComparisons(n):
    if n == 1:
        return 0
    else:
        return n-1 + mergeComparisons(math.ceil(n/2)) + mergeComparisons(math.floor(n/2))

# print(mergeComparisons(153))
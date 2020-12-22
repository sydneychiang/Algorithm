def BS1(A, x):
    first = 0
    last = len(A)-1
    while first < last:
        index = (first + last)//2
        if x == A[index]:
            return index
        elif x < A[index]:
            last = index - 1
        else:
            first = index + 1
    return -1

# print(BS1([0,1,2,3,4,5,6], 4))


def BS2(A, x):
    first = 0
    last = len(A)-1
    while first <= last:
        index = (first + last)//2
        print("first: ", first, " ", "last: ", last, " ", "index: ", index)
        if x == A[index]:
            return index
        elif x < A[index]:
            last = index
        else:
            first = index + 1
    return -1

print(BS2([0,1,2,3,4,5,6], -1))
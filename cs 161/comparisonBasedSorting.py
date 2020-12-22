# Comparison-based sorting:
# Merge sort, including its use for counting inversions
# Priority queues
# Binary heaps: basic properties, sift-up, sift-down, insertion, deletion, construction
# Heap sort
# Lower bounds on comparison-based sorting
# Optimally sorting 5 elements
import math;


#MERGE SORT WITHOUT INVERSIONS
# Running time: = Θ(n log n)
# A - input list
# first - first index
# last - last index
# def mergeSort(A,first,last):
#     if first < last:
#         mid = math.floor((first + last)/2)
#         mergeSort(A,first,mid)
#         mergeSort(A,mid+1,last)
#         merge(A,first,mid,mid+1,last)
#
#
# def merge(A,first1,last1,first2,last2):
#     index1 = first1
#     index2 = first2
#     tempIndex = 0
#
#     temp = []
#     for i in range(len(A)):
#         temp.append(0)
#
#     # Merge into temp array until one input array is exhausted
#     while (index1 <= last1) and (index2 <= last2):
#         if A[index1] <= A[index2]:
#             temp[tempIndex] = A[index1]
#             tempIndex += 1
#             index1 += 1
#         else:
#             temp[tempIndex] = A[index2]
#             tempIndex += 1
#             index2 += 1
#     # Copy appropriate trailer portion
#     while (index1 <= last1):
#         temp[tempIndex] = A[index1]
#         tempIndex += 1
#         index1 += 1
#     while (index2 <= last2):
#         temp[tempIndex] = A[index2]
#         tempIndex+=1
#         index2 += 1
#
#     # Copy temp array back to A array
#     tempIndex = 0
#     index = first1
#     while (index <= last2):
#         A[index] = temp[tempIndex]
#         index += 1
#         tempIndex += 1
#
#     print(A)


# A = [19, 26, 42, 71, 14, 24, 31, 39]
# X = [10, 28, 65, 89] Y = [20, 25, 41, 47]
X = [10, 28, 65, 89, 20, 25, 41, 47]
# print(X)
# mergeSort(X, 0, 4)
# print(X)
# print(A)
# mergeSort(A, 0, 7)
# print(A)


# MERGE SORT WITH INVERSIONS
# Running time: O(n log n)
# A - input list
# first - first index
# last - last index
def mergeSort(A,first,last):
    invCount = 0

    if first < last:
        mid = math.floor((first + last)/2)
        invCount += mergeSort(A,first,mid)
        invCount += mergeSort(A,mid+1,last)
        invCount += merge(A,first,mid,mid+1,last)
        print(A, invCount)
    return invCount

def merge(A,first1,last1,first2,last2):
    index1 = first1
    index2 = first2
    tempIndex = 0
    invCount = 0
    # print(A)
    temp = []
    for i in range(len(A)):
        temp.append(0)

    # Merge into temp array until one input array is exhausted
    while (index1 <= last1) and (index2 <= last2):
        if A[index1] <= A[index2]:
            # print(A, invCount, A[index1], A[index2])
            temp[tempIndex] = A[index1]
            tempIndex += 1
            index1 += 1
        else:
            temp[tempIndex] = A[index2]
            tempIndex += 1
            index2 += 1
            invCount += last1 - index1 + 1
        print(A, invCount, index1, index2)
    # Copy appropriate trailer portion
    while (index1 <= last1):
        temp[tempIndex] = A[index1]
        tempIndex += 1
        index1 += 1
    while (index2 <= last2):
        temp[tempIndex] = A[index2]
        tempIndex += 1
        index2 += 1
    # Copy temp array back to A array
    tempIndex = 0
    index = first1
    while (index <= last2):
        A[index] = temp[tempIndex]
        index += 1
        tempIndex += 1
    return invCount

A = [26,27,19,17,47,80,28,60,25,29,18,43]
print(A)
inv = mergeSort(A, 0, 11)
print(A, inv)
# print(A, inv)

# BINARY HEAPS / HEAP SORT
# this is not a functional version

def FindMax(H):
    return H[0]

def SiftUp(H,i):
    parent = (i-1)/2;
    if (i > 0) and (H[parent].key < H[i].key):
        H[i], H[parent] = H[parent], H[i]
        SiftUp(H,parent)

def Insert(H,x):
    H.size = len(H)+1 # increment number of items UH
    k = len(H)-1 #index of last position
    H[k] = x #insert x in last position
    SiftUp(H,k)


def Delete(H,i):
    k = len(H)-1 #index of last position
    H[i] = H[k] # overwrite item being deleted with element in last position
    H.size = H.size-1 #decrement number of item
    SiftUp(H,i) #either SiftUp or SiftDown will do nothing
    SiftDown(H,i)


def ExtractMax(H):
    x = H[0]
    Delete(H,0)
    return x


# MAX-HEAP
def SiftDown(H,i):
    n = len(H) #number of item in heap
    left = 2*i+1
    right = 2*i+2
    if (right < n) and (H[right] > H[left]):
        largerChild = right
    else:
        largerChild = left
    if (largerChild < n) and (H[i] < H[largerChild]):
        H[i], H[largerChild] = H[largerChild], H[i]
        SiftDown(H,largerChild)

# # MIN-HEAP
# def SiftDown(H,i):
#     n = len(H) #number of item in heap
#     left = 2*i+1
#     right = 2*i+2
#     if (right < n) and (H[right] < H[left]):
#         largerChild = right
#     else:
#         largerChild = left
#     if (largerChild < n) and (H[i] > H[largerChild]):
#         H[i], H[largerChild] = H[largerChild], H[i]
#         SiftDown(H,largerChild)


def recHeapify(H, k):
    if (2*k+1) <= len(H):
        recHeapify(H, 2*k+1)
    if(2*k+2) <= len(H):
        recHeapify(H, 2*k+2)
    SiftDown(H, k)

# H = [70, 25, 68, 35, 65, 42, 88, 13, 8, 17, 89, 39, 22, 96, 48]
H = [20, 94, 57, 14, 21, 67, 54, 77, 68, 48, 83, 70, 71]
recHeapify(H, 0)
print(H)


# LOWER BOUND OPTIMAL COMPARISON?
# Amount of comparisons: ceil(log n!)
# Optimally sorting 5 items with 7 comparisons
def lowerBound (A, B, C, D, E):
    if A > B:
        A, B = B, A
    if (C > D):
        C, D = D, C
    if (A > C):
        A, C = C,A
        B,D = D,B # Thanks Deqing!

    if (E > C):
        if (E > D):  # A C D E
            if (B > D):
                if (B > E):
                    return (A, C, D, E, B)
                else:
                    return (A, C, D, B, E)
            else:
                if (B < C):
                    return (A, B, C, D, E)
                else:
                    return (A, C, B, D, E)

        else:  # A C E D
            if (B > E):
                if (B > D):
                    return (A, C, E, D, B)
                else:
                    return (A, C, E, B, D)
            else:
                if (B < C):
                    return (A, B, C, E, D)
                else:
                    return (A, C, B, E, D)
    else:
        if (E < A):  # E A C D
            if (B > C):
                if (B > D):
                    return (E, A, C, D, B)
                else:
                    return (E, A, C, B, D)
            else:
                 return (E, A, B, C, D)

        else:  # A E C D
            if (B > C):
                if (B > D):
                    return (A, E, C, D, B)
                else:
                    return (A, E, C, B, D)
            else:
                if (B < E):
                    return (A, B, E, C, D)
                else:
                    return (A, E, B, C, D)



A = [8,10,3,7,2]
A = lowerBound(A[0], A[1], A[2], A[3], A[4])
# print(A)








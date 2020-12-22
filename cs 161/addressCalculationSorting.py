# ADDRESS-CALCULATION SORTING


# COUNTING SORT
# Running time: O(n + k)
# A - input array unsorted
# B - output array sorted
# n - length of A
# k - each integer in A is within [1, k]
def CountingSort(A, B, n , k):
    # Initialize: set each locator[x] to
    # the number of entries ≤ x
    locator=[]
    for x in range(1,k):
        locator.append(0)

    for i in range (1, n):
        locator[A[i]] = locator[A[i]] + 1

    for x in range(2, k-1):
        locator[x] = locator[x] + locator[x-1]

    #Fill output array, updating locator values
    for i in range(n-1, 0, -1):
        # print(B)
        B[locator[A[i]]] = A[i]
        locator[A[i]] = locator[A[i]] - 1


A = [0,2,2,3,1,3,3,3,1]
B = []
for i in range(len(A)):
    B.append(0)
CountingSort(A, B, len(A), 10)


# BUCKET SORT
# Worst-case: O(n^2)
# Best-case: O(n)
# x - Array to sort
# b - element to sort into the array
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

        # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

        # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

        # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# Driver Code
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
# print("Sorted Array is")
# print(bucketSort(x))



# RADIX SORT: INSERTION SORT
# Running time: O(d(n + b))
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        # countingSort(arr, exp)
        exp *= 10


# def countingSort(arr, exp1):
#
#     n = len(arr)
#
# 	# The output array elements that will have sorted arr
# 	output = [0] * (n)
#
# 	# initialize count array as 0
# 	count = [0] * (10)
#
# 	# Store count of occurrences in count[]
# 	for i in range(0, n):
# 		index = (arr[i] / exp1)
# 		count[int(index % 10)] += 1
#
# 	# Change count[i] so that count[i] now contains actual
# 	# position of this digit in output array
# 	for i in range(1, 10):
# 		count[i] += count[i - 1]
#
# 	# Build the output array
# 	i = n - 1
# 	while i >= 0:
# 		index = (arr[i] / exp1)
# 		output[count[int(index % 10)] - 1] = arr[i]
# 		count[int(index % 10)] -= 1
# 		i -= 1
#
# 	# Copying the output array to arr[],
# 	# so that arr now contains sorted numbers
# 	i = 0
# 	for i in range(0, len(arr)):
# 		arr[i] = output[i]


# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
radixSort(arr)
# print(arr)

# for i in range(len(arr)):
# 	print(arr[i])

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher




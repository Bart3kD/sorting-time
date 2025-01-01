import math
from heapq import heappush, heappop


# The main function to sort
# an array of the given size
# using heap_sort algorithm
def heap_sort(arr):
    h = []

    # building the heap
    for value in arr:
        heappush(h, value)

    # extracting the sorted elements one by one
    return [heappop(h) for _ in range(len(h))]


# The main function to sort the data using
# insertion sort algorithm
def insertion_sort(arr, begin, end):
    left = begin
    right = end

    # Traverse through 1 to len(arr)
    for i in range(left + 1, right + 1):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    # pivot
    pivot = arr[high]

    # index of smaller element
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or
        # equal to the pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# The function to find the median
# of the three elements in
# in the index a, b, d
def median_of_three(arr, a, b, d):
    A = arr[a]
    B = arr[b]
    C = arr[d]

    if A <= B <= C or C <= B <= A:
        return b
    if B <= A <= C or C <= A <= B:
        return a
    return d


# The main function that implements introsort
# low --> Starting index,
# high --> Ending index
# depthLimit --> recursion level
def introsort_util(arr, begin, end, depthLimit):
    size = end - begin
    if size < 16:
        # if the data set is small, call insertion sort
        insertion_sort(arr, begin, end)
        return

    if depthLimit == 0:
        # if the recursion limit is occurred, call heap sort
        arr[begin:end + 1] = heap_sort(arr[begin:end + 1])
        return

    pivot = median_of_three(arr, begin, begin + size // 2, end)
    arr[pivot], arr[end] = arr[end], arr[pivot]

    # partitionPoint is partitioning index,
    # arr[partitionPoint] is now at right place
    partitionPoint = partition(arr, begin, end)

    # Separately sort elements before partition and after partition
    introsort_util(arr, begin, partitionPoint - 1, depthLimit - 1)
    introsort_util(arr, partitionPoint + 1, end, depthLimit - 1)


# A utility function to begin the introsort module
def intro_sort(array):
    n = len(array)
    depthLimit = 2 * math.floor(math.log2(n))
    introsort_util(array, 0, n - 1, depthLimit)
    return array


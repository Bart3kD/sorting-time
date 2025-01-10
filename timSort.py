from insertionSort import insertion_sort

def tim_sort(arr: list[int]) -> list[int]:
    """
    Tim sort algorithm

    :param arr: Unsorted list

    :return: Sorted list of integers
    """
    def binary_search(arr, item, start, end):
        if start == end:
            return start if arr[start] > item else start + 1
        if start > end:
            return start

        mid = (start + end) // 2
        if arr[mid] < item:
            return binary_search(arr, item, mid + 1, end)
        elif arr[mid] > item:
            return binary_search(arr, item, start, mid - 1)
        else:
            return mid

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left

        if left[0] < right[0]:
            return [left[0], *merge(left[1:], right)]

        return [right[0], *merge(left, right[1:])]

    length = len(arr)
    runs, sorted_runs = [], []
    new_run = [arr[0]]
    sorted_array = []
    i = 1
    while i < length:
        if arr[i] < arr[i - 1]:
            runs.append(new_run)
            new_run = [arr[i]]
        else:
            new_run.append(arr[i])
        i += 1
    runs.append(new_run)

    for run in runs:
        sorted_runs.append(insertion_sort(run))
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array
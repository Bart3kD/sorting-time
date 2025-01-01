def swap(arr: list[int], i: int , j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i + 1

def q_sort(arr: list[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)

        q_sort(arr, low, pi - 1)
        q_sort(arr, pi + 1, high)

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    return q_sort(arr, 0, len(arr) - 1)
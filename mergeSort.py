def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_list = []
    l, r = 0, 0
    while l != len(left) or r != len(right):
        if l == len(left):
            sorted_list.append(right[r])
            r += 1
        elif r == len(right):
            sorted_list.append(left[l])
            l += 1
        elif left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    return sorted_list

def m_sort(lo: int, hi: int, arr: list[int]) -> list[int]:
    if lo == hi:
        return [arr[lo]]
    
    mid = (lo + hi) // 2

    left = m_sort(lo, mid, arr)
    right = m_sort(mid + 1, hi, arr)

    return merge(left, right)

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) == 0:
        return []
    return m_sort(0, len(arr) - 1, arr)

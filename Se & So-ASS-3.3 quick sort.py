def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_half = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_half = [x for x in arr if x > pivot]

    return quick_sort(left_half) + middle + quick_sort(right_half)

arr = [80, 44, 34, 54, 9, 5, 1, 3]
print(quick_sort(arr))

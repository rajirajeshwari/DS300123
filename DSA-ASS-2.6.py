import random

def partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, k, low, high):
    if low == high:
        return arr[low]
    pivot_idx = partition(arr, low, high)
    if pivot_idx == k:
        return arr[k]
    elif pivot_idx < k:
        return quickselect(arr, k, pivot_idx + 1, high)
    else:
        return quickselect(arr, k, low, pivot_idx - 1)

def find_kth_largest(arr, k):
    return quickselect(arr, len(arr) - k, 0, len(arr) - 1)

def find_kth_smallest(arr, k):
    return quickselect(arr, k - 1, 0, len(arr) - 1)

arr = [3, 7, 1, 8, 4, 2, 5, 6]
k = 3
kth_largest = find_kth_largest(arr, k)
print(kth_largest)

k = 4
kth_smallest = find_kth_smallest(arr, k)
print(kth_smallest)

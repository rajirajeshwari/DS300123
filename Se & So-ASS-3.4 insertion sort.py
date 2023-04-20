def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_val
    return arr

# Example usage
arr = [20, 15, 5, 10, 50, 30, 45, 25, 50]
print(insertion_sort(arr))

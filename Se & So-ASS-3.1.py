def binary_search(arr, search_element):
    """
    Searches for the given target value in the sorted array arr using binary search algorithm.
    Returns the index of the target value if found, otherwise returns -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == search_element:
            return mid
        elif arr[mid] < search_element:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
arr = [1, 3, 5, 7, 9]
search_element = 5

index = binary_search(arr, search_element)
if index == -1:
    print("Search_Element value not found in the array.")
else:
    print(f"Search_Element value found at index {index}.")

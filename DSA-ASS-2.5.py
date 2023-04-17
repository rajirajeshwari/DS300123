def find_duplicates(arr: list[int]) -> list[int]:
    unique_set = set()
    duplicates = []
    for num in arr:
        if num in unique_set:
            duplicates.append(num)
        else:
            unique_set.add(num)
    return duplicates
arr = [1, 3, 4, 2, 2, 3, 1, 7]
duplicates = find_duplicates(arr)
print(duplicates)

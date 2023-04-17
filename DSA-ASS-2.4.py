def count_pairs_with_sum(arr: list[int], target_sum: int) -> int:
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    count = 0
    for num in arr:
        freq_map[num] -= 1
        complement = target_sum - num
        if complement in freq_map and freq_map[complement] > 0:
            count += freq_map[complement]
        freq_map[num] += 1
    return count
arr = [1, 5, 7, -1, 5]
target_sum = 6
count = count_pairs_with_sum(arr, target_sum)
print(count)

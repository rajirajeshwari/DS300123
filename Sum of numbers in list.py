def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = (8, 2, 3, 0, 7)
result = sum_list(my_list)
print(result)
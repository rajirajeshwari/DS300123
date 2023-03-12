def triple(x):
    return x * 3

my_list = [1, 2, 3, 4, 5, 6, 7]
triple_list = list(map(triple, my_list))
print(triple_list)
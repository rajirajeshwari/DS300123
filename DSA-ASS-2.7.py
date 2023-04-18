def move_negative(arr):
    neg_arr = []
    pos_arr = []
    for i in arr:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    return neg_arr + pos_arr
arr = [-1, 2, -3, 4, 5, 6, -7, 8, -9]
result = move_negative(arr)
print(result)

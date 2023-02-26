my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def get_last_element(t):
    return t[-1]
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if get_last_element(my_list[i]) > get_last_element(my_list[j]):
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
print(my_list)


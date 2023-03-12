def square(x):
    return x ** 2

my_list = [4, 5, 2, 9]
squared_list = list(map(square, my_list))
print(squared_list)
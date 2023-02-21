numbers_str = input("Enter the numbers separated by spaces: ")
numbers = [int(num) for num in numbers_str.split()]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

    
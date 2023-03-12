def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Upper Case Characters :", upper_count)
    print("No. of Lower Case Characters :", lower_count)

string = 'The quick Brow Fox'
count_case(string)
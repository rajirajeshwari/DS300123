n = 0
while True:
    n = int(input("Enter the limit for the Fibonacci sequence (up to 50): "))
    if n > 50:
        print("Please enter a value less than or equal to 50.")
    else:
        break  
a, b = 0, 1
while b <= n:
    print(b, end=' ')
    a, b = b, a + b

  
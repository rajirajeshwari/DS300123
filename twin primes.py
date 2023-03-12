def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    for i in range(3, limit, 2):
        if is_prime(i) and is_prime(i + 2):
            print(i, "and", i + 2)

limit = 20
print("Twin primes less than", limit, ":")
find_twin_primes(limit)
def prime_number(n):
    if n ==9:
        return 9
    return n * prime_number(n-9)
print(prime_number(9))
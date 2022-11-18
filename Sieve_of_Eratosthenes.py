def sieve(n):
    prime_numbers = list(range(n + 1))

    prime_numbers[1] = 0
    i = 2
    while i <= n:
        if prime_numbers[i] != 0:
            j = i + i
            while j <= n:
                prime_numbers[j] = 0
                j = j + i
        i += 1

    prime_numbers = set(prime_numbers)
    prime_numbers.remove(0)
    
    return sorted(prime_numbers)

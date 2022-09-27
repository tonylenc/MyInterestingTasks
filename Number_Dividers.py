def dividers(n):
    res = []
    i = 2

    while i * i <= n:
        if n % i == 0:
            res.append(i)

            if n != i**2:
                res.append(n // i)

        i += 1

    res.extend([1, n])
    res.sort()

    return res

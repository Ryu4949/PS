def moss(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    k = 0
    while True:
        if n <= 2**k:
            k -= 1
            break

        k += 1

    return 1 - moss(n - 2**k)

N = int(input())
print(moss(N))
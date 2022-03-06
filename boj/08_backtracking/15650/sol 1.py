#좀더 간결하게 될거같은데..

N, M = map(int, input().split())
num_list = list(range(1, N+1))
bit = [0] * N

def subset(a, i, n):
    if i == n:
        if sum(a) == M:
            for j in range(n):
                if a[j]:
                    print(num_list[j], end=" ")
            print()
        return

    if sum(a) == M:
        for j in range(n):
            if a[j]:
                print(num_list[j], end=" ")
        print()
        return
    else:
        a[i] = 1
        subset(a, i+1, n)
        a[i] = 0
        subset(a, i+1, n)

subset(bit, 0, N)
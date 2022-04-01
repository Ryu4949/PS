a = [1, 2, 3, 4]
N = len(a)

for i in range(1, 1<<N):
    for j in range(N):
        if i & (1<<j):
            print(a[j], end=' ')
    print()
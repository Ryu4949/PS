t = int(input())
for num in range(1, t + 1):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    print(f'#{num}', end=" ")
    for i in a:
        print(i, end=" ")
    print()
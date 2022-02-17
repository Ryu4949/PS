T = int(input())
for tc in range(1, T+1):
    n = int(input())
    info = list(map(int, input().split()))

    profit = 0
    j = n-1
    for i in range(n-1, -1, -1):
        if info[i] <= info[j]:
            profit += info[j]-info[i]
        else:
            j = i

    print(f'#{tc} {profit}')
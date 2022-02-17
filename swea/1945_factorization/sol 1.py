T = int(input())
for tc in range(1, T+1):
    fac = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    n = input()
    s = int(n)

    j = 0
    while s > 1:
        if s % fac[j] == 0:
            cnt[j] += 1
            s /= fac[j]
        else:
            j += 1

    print(f'#{tc}', end=" ")
    for i in cnt:
        print(i, end=" ")
    print()

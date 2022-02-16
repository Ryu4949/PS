for num in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        if buildings[i] != max(buildings[i-2:i+3]):
            continue
        else:
            cnt += buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])

    print(f'#{num} {cnt}')
t = int(input())
for num in range(1, t+1):
    n, m = map(int, input().split())
    fly = []
    for _ in range(n):
        fly.append(list(map(int, input().split())))

    max_fly = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly_area = []
            for k in range(m):
                fly_area += fly[j+k][i:i+m]
            if sum(fly_area) > max_fly:
                max_fly = sum(fly_area)

    print(f'#{num} {max_fly}')
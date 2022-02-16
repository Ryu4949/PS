t = int(input())
for num in range(1, t+1):
    n, m = map(int, input().split())
    fly = []
    for _ in range(n):
        fly.append(list(map(int, input().split())))

    def sum_fly(row, col):
        cnt = 0
        for x in range(row, row+m):
            for y in range(col, col+m):
                cnt += fly[x][y]
        return cnt

    max_fly = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            if sum_fly(i, j) > max_fly:
                max_fly = sum_fly(i, j)

    print(f'#{num} {max_fly}')
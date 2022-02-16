t = int(input())
for num in range(1, t+1):
    n, k = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    cnt = 0
    for i in range(n):
        length = 0
        for j in range(n):
            length += data[i][j]

            if data[i][j] == 1 and length == k:
                if j == n-1 or data[i][j+1] == 0:
                    cnt += 1
                    length = 0
            elif data[i][j] == 0:
                length = 0

    for i in range(n):
        length = 0
        for j in range(n):
            length += data[j][i]

            if data[j][i] == 1 and length == k:
                if j == n-1 or data[j+1][i] == 0:
                    cnt += 1
                    length = 0
            elif data[j][i] == 0:
                length = 0

    print(f'#{num} {cnt}')
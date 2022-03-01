N = int(input())
M = int(input())
INF = int(1e9)

distance = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            distance[i][j] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
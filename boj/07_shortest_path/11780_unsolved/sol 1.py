N = int(input())
M = int(input())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
path = [[[] for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if distance[a][b] > c:
        distance[a][b] = c
        path[a][b].extend([a, b])

for i in range(N+1):
    for j in range(N+1):
        if i == j:
            distance[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                path[i][j] = path[i][k][:]
                for v in path[k][j]:
                    if v not in path[i][j]:
                        path[i][j].append(v)

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if not path[i][j]:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])
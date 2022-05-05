N, M = map(int, input().split())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    distance[a][b] = 1

for i in range(1, N+1):
    distance[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

ans = 0
for i in range(1, N+1):
    light = 0
    heavy = 0
    for j in range(1, N+1):
        if j != i and distance[j][i] < float('inf'):
            light += 1
        elif j != i and distance[i][j] < float('inf'):
            heavy += 1

    if heavy > N//2 or light > N//2:
        ans += 1

print(ans)
N = int(input())
M = int(input())
distance = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        if i == j:
            distance[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    distance[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i != j and distance[i][j] == float('inf') and distance[j][i] == float('inf'):
            cnt += 1
    print(cnt)
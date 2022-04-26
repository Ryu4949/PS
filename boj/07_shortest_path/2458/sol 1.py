N, M = map(int, input().split())
distance = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    distance[a-1][b-1] = 1

for i in range(N):
    distance[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

ans = 0
for i in range(N):
    for j in range(N):
        if distance[i][j] == float('inf') and distance[j][i] == float('inf'):
            break
    else:
        ans += 1

print(ans)
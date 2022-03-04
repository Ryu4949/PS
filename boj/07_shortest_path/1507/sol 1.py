N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
road = [[True] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j:
                road[i][j] = False
                break

            if i != k and j != k and graph[i][j] == graph[i][k] + graph[k][j]:
                road[i][j] = False
                break

            elif graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit(0)

ans = 0
for i in range(N):
    for j in range(i, N):
        if road[i][j]:
            ans += graph[i][j]

print(ans)
N, K = map(int, input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

S = int(input())
for _ in range(S):
    a, b = map(int, input().split())
    if graph[a][b] < float('inf'):
        print(-1)
    elif graph[b][a] < float('inf'):
        print(1)
    else:
        print(0)
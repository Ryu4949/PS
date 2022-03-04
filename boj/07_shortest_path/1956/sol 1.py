V, E = map(int, input().split())
graph = [[float('inf')] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

cycle = 0
ans = float('inf')
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            cycle = graph[i][j] + graph[j][i]
            ans = min(ans, cycle)

if ans == float('inf'):
    ans = -1

print(ans)

N, M = map(int, input().split())
INF = int(1e9)

#파티장 번호랑 인덱스랑 맞도록
graph = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

#플-와
for k in range(1, N+1):
    for r in range(1, N+1):
        for c in range(1, N+1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
N, M, R = map(int, input().split())
INF = int(1e9)

items = list(map(int, input().split()))

graph = [[INF] * N for _ in range(N)]

#방향없이 두 정점간 거리를 나타내므로 양쪽 모두에 거리 설정
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

#자기 자신으로의 거리는 0
for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

#플로이드-와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#순서대로 낙하지점을 지정하고 해당 지점에 낙하할 경우 얻을 수 있는 아이템의 최대 개수를 갱신
max_item = 0
for i in range(N):
    item = 0
    for j in range(N):
        if graph[i][j] <= M:
            item += items[j]
    max_item = max(max_item, item)

print(max_item)
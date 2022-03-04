import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
INF = int(1e9)

distance = [INF] * (V+1)

#a: 노드, b: 연결된 노드, c: 거리
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        #이미 출발점부터 now까지 거리가 dist보다 짧다면 이하 무시
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
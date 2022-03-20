import heapq

N, M = map(int, input().split())
vision = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

vision[-1] = 0
distance = [float('inf')] * N

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if not vision[i[0]]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra()

print(distance[N-1]) if distance[N-1] != float('inf') else print(-1)
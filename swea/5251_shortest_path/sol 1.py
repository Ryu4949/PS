import heapq
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    INF = int(1e9)
    distance = [INF] * (N+1)

    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstra():
        q = []
        distance[0] = 0
        heapq.heappush(q, (0, 0))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra()

    print(f'#{tc} {distance[N]}')

#다익스트라로 N번 돌려보기
#일단 실패
import heapq

N, M, R = map(int, input().split())
INF = int(1e9)

items = [0] + list(map(int, input().split()))

distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

max_item = 0
for i in range(1, N+1):
    dijkstra(i)
    item = 0
    for j in range(1, N+1):
        if distance[j] <= M:
            item += items[j]

    max_item = max(max_item, item)

print(max_item)
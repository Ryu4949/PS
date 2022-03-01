import heapq

N, D = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(D+1)]
distance = [i for i in range(D+1)]

q = []

for _ in range(N):
    a, b, c = map(int, input().split())
    if a <= D and b <= D and b-a > c:
        heapq.heappush(q, ())

print(f'graph: {graph}')

def dijkstra(start):
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)

print(f'변경전: {distance}')
for i in range(1, D+1):
    distance[i] = min(distance[i], distance[i-1]+1)

print(f'변경후: {distance}')
print(distance[D])
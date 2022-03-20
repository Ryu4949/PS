import heapq
#1번 노드에서 다른 노드들까지 가는 최단 경로 저장하기

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

path = [[] for _ in range(N+1)]

distance = [float('inf')] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    path[start].append(start)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                path[i[0]] = path[now] + [i[0]]

dijkstra(start)

print(path)


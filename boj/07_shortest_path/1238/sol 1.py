import heapq
import sys
input = sys.stdin.readline

def dijkstra(v):
    q = []
    heapq.heappush(q, (0, v))
    distance[v] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

to_home = None
time = [0] * (N+1)
for i in range(1, N+1):
    distance = [float('inf')] * (N + 1)
    dijkstra(i)
    if i == X:
        to_home = distance[:]
    else:
        time[i] = distance[X]

answer = 0
for i in range(1, N+1):
    answer = max(answer, to_home[i]+time[i])

print(answer)
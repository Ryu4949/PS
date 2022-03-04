import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
distance = [float('inf')] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, g = map(int, input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

dijkstra(s)

print(distance[g])
'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
ans: 7
'''

import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = 1
graph = [[] for _ in range(V+1)]
distance = [float('inf')] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
necessary = list(map(int, input().split()))
waypoint = [[] for _ in range(V+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    waypoint[start].append(start)

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                waypoint[i[0]] = waypoint[now] + [i[0]]

            elif i[0] in necessary and i[0] not in waypoint[now]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                waypoint[i[0]] = waypoint[now] + [i[0]]

dijkstra(start)

print(waypoint)

ans = distance[-1]
if ans == float('inf'):
    print(-1)
else:
    print(ans)
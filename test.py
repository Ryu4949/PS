import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (V+1)
distance = [INF] * (V+1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for _ in range(V-1):
        now = get_smallest_node()
        visited[now] = True

        for i in graph[now]:
            cost = distance[now] + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
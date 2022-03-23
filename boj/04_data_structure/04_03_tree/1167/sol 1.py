from collections import deque

def bfs(v):
    distance = [-1] * (V+1)
    queue = deque([v])
    distance[v] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if distance[i[0]] == -1:
                distance[i[0]] = distance[v] + i[1]
                queue.append(i[0])

    return (max(distance), distance.index(max(distance)))

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    edge = list(map(int, input().split()))
    node = edge[0]
    for i in range(1, len(edge)-1, 2):
        graph[node].append((edge[i], edge[i+1]))

one_end = bfs(1)[1]

print(bfs(one_end)[0])
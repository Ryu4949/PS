from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1

for tc in range(1, 11):
    N, root = map(int, input().split())
    edge = list(map(int, input().split()))
    V = max(edge)
    graph = [[] for _ in range(V+1)]
    for i in range(N//2):
        graph[edge[2*i]].append(edge[2*i+1])

    visited = [-1] * (V+1)

    bfs(root)

    for i in range(V, 0, -1):
        if visited[i] == max(visited):
            print(f'#{tc} {i}')
            break
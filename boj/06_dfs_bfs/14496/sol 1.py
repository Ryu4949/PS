from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 0

    while queue:
        x = queue.popleft()
        
        for v in graph[x]:
            if visited[v] == -1:
                queue.append(v)
                visited[v] = visited[x]+1

bfs(a)

print(visited[b])
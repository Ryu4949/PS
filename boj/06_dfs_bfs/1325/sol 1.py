from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
cnt = [0] * (N+1)

def bfs(start, graph):
    visited = [False] * (N+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited.count(True)

for i in range(1, N+1):
    cnt[i] = bfs(i, graph)

max_cnt = max(cnt)
for i in range(1, N+1):
    if cnt[i] == max_cnt:
        print(i, end=" ")

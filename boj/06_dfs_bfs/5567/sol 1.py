from collections import deque

def bfs():
    queue = deque([1])
    visited[1] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

ans = 0
for i in range(1, N+1):
    if 1<=visited[i]<=2:
        ans += 1

print(ans)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)

def dfs(n):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
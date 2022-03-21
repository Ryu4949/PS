def dfs(v):
    stack = [v]
    visited = [False] * (N+1)
    visited[v] = True

    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                nodes[i] = v

N = int(input())
nodes = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(nodes[i])
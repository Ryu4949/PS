N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [-1] * (N+1)
visited[A] = 0
def dfs(n):
    for i in graph[n]:
        if visited[i] == -1:
            visited[i] = visited[n] + 1
            dfs(i)

dfs(A)

print(visited[B])
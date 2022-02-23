T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    S, G = map(int, input().split())
    visited = [False] * (V + 1)

    def dfs(graph, start):
        visited[start] = True

        for i in graph[start]:
            if not visited[i]:
                dfs(graph, i)

    dfs(graph, S)
    
    if visited[G] == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
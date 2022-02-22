for _ in range(10):
    m, n = map(int, input().split())
    graph = [[] for _ in range(100)]
    edge = list(map(int, input().split()))
    for i in range(n):
        graph[edge[2*i]].append(edge[2*i+1])

    visited = [False] * 100

    def dfs(start, visited, graph):
        stack = [start]
        visited[start] = True

        while stack:
            v = stack.pop()
            for i in graph[v]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True

    dfs(0, visited, graph)

    if visited[99]:
        print(f'#{m} 1')
    else:
        print(f'#{m} 0')
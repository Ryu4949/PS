tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    visited = [False] * (N+1)


    def dfs(v):
        stack = [v]
        visited[v] = True

        while stack:
            v = stack.pop()

            for i in graph[v]:
                if visited[i]:
                    return False
                else:
                    visited[i] = True
                    stack.append(i)
        return True

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
           if dfs(i):
               cnt += 1
           else:
               cnt = 0
               break

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
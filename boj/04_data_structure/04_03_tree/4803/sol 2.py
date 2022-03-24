#트리의 간선의 개수는 정점 개수 -1 개이므로 그런 성질을 이용해봤으나 이것도 실패~
#사이클의 존재 여부를 어떻게 판단해야 할까?

def dfs(v):
    stack = [v]
    visited[v] = True
    vertex = 1
    edge = 0

    while stack:
        v = stack.pop()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                vertex += 1
                edge += 1
            else:
                edge += 1
    if edge//2 == vertex-1:
        return True
    else:
        return False

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
        graph[b].append(a)
    visited = [False] * (N+1)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
           if dfs(i):
               cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')
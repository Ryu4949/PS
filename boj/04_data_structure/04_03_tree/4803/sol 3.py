'''
아이디어:
간선에 방향이 없지만, 한쪽에만 간선 정보를 저장해 주었다.
이유는 사이클의 존재 여부를 한번 방문한 곳에 다시 연결되어있는지 여부로 판단하기 위함인데
간선정보를 양쪽 모두에 저장하게 된다면
'''

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
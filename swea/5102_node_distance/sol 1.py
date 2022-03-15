from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    #최소거리 저장할 리스트. -1이면 아직 방문하지 않은 상태를 의미
    check = [-1] * (V+1)

    #간선정보 담기
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    #출발점과 도착점
    S, G = map(int, input().split())

    def bfs(v):
        #출발점에 check를 0으로 설정하고 큐에추가
        queue = deque([v])
        check[v] = 0

        while queue:
            #큐에서 하나씩 pop해서
            v = queue.popleft()

            #해당 노드와 인접한 노드들에 대해
            for i in graph[v]:
                #아직 방문하지 않았다면 큐에 추가하고 최소거리 갱신
                if check[i] == -1:
                    queue.append(i)
                    check[i] = check[v] + 1

    #시작점에서 bfs
    bfs(S)

    print(f'#{tc} {max(0, check[G])}')
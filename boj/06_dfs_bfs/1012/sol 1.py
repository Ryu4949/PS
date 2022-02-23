from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # <RecrsionError> 판정을 받기 때문에 재귀를 사용하지 않는 bfs로 다시시도
    # def dfs(r, c):
    #     if 0<=r<N and 0<=c<M and graph[r][c] == 1:
    #         graph[r][c] = 0
    #         for i in range(4):
    #             rr = r + dr[i]
    #             cc = c + dc[i]
    #             dfs(rr, cc)
    #         return True
    #     else:
    #         return False
    #
    # cnt = 0
    # for r in range(N):
    #     for c in range(M):
    #         if dfs(r, c) == True:
    #             cnt += 1
    #
    # print(cnt)

    def bfs(x, y):
        if graph[x][y] == 1:
            queue = deque([(x, y)])
            graph[x][y] = 0

            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    rr = r + dr[i]
                    cc = c + dc[i]
                    if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 1:
                        queue.append((rr, cc))
                        graph[rr][cc] = 0

            return True
        else:
            return False

    cnt = 0
    for x in range(N):
        for y in range(M):
            if bfs(x, y) == True:
                cnt +=1

    print(cnt)
from collections import deque

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            if loc[graph[r][c]][i]:
                rr, cc = r+dr[i], c+dc[i]

                if 0<=rr<N and 0<=cc<M and visited[rr][cc] == -1 and loc[graph[rr][cc]][(i+2)%4]:
                    queue.append((rr, cc))
                    visited[rr][cc] = visited[r][c] + 1


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    #상좌하우
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    loc = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0]]

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0<=visited[i][j]<=L:
                cnt += 1

    print(f'#{tc} {cnt}')
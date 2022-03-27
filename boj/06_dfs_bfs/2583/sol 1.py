from collections import deque

M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

area = []

def bfs(r, c):
    cnt = 1
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<M and 0<=cc<N and not visited[rr][cc] and board[rr][cc] == 0:
                cnt += 1
                visited[rr][cc] = True
                queue.append((rr, cc))

    area.append(cnt)

for i in range(M):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 0:
            bfs(i, j)

area.sort()
print(len(area))
print(*area)
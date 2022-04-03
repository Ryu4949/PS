from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]

empty = []
bombs = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        if board[i][j] == 2:
            bombs.append((i, j))

empty_lst = list(combinations(empty, 3))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    for i in bombs:
        queue.append(i)

    for r, c in bombs:
        visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and board[rr][cc] == 0:
                queue.append((rr, cc))
                visited[rr][cc] = True

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visited[i][j]:
                cnt += 1

    return cnt

ans = 0
for i in empty_lst:
    for x, y in i:
        board[x][y] = 1
    safe = bfs()
    ans = max(ans, safe)

    for x, y in i:
        board[x][y] = 0

print(ans)

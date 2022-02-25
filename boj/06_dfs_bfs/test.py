from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())

    dr = [2, 1, -1, -2, -2, -1, 1, 2]
    dc = [-1, -2, -2, -1, 1, 2, 2, 1]

    board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    def bfs(r, c):
        queue = deque([(r, c)])
        if sx == gx and sy == gy:
            return 0

        while queue:
            r, c = queue.popleft()

            for i in range(8):
                rr, cc = r+dr[i], c+dc[i]
                if 0<=rr<N and 0<=cc<N and board[rr][cc] == 0:
                    queue.append((rr, cc))
                    board[rr][cc] = board[r][c] + 1

                    if (rr, cc) == (gx, gy):
                        return board[rr][cc]

    print(bfs(sx, sy))
from collections import deque

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r, c = 1, 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    visited = [[-1] * 4 for _ in range(4)]
    queue = deque([(r, c)])
    visited[r][c] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<4 and 0<=cc<4 and visited[rr][cc] == -1:
                if board[rr][cc] > 0:
                    visited[rr][cc] = visited[r][c] + 1
                    queue.append((rr, cc))
                else:
                    if

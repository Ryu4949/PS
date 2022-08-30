import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    color = graph[r][c]
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        if graph[r][c] == "G":
            graph[r][c] = "R"

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and graph[rr][cc] == color:
                queue.append((rr, cc))
                visited[rr][cc] = True

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = [0, 0]
for k in range(2):
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt[k] += 1
                bfs(i, j)

print(*cnt)
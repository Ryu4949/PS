from collections import deque

def bfs(r, c):
    if graph[r][c] == 'W':
        return 0

    visited = [[False] * M for _ in range(N)]
    queue = deque([(r, c, 0)])
    visited[r][c] = True

    while queue:
        r, c, d = queue.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 'L' and not visited[rr][cc]:
                queue.append((rr, cc, d+1))
                visited[rr][cc] = True
    return d

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
for i in range(N):
    for j in range(M):
        dist = bfs(i, j)
        ans = max(ans, dist)

print(ans)
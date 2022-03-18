from collections import deque

def bfs(r, c, h):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and graph[rr][cc] > h:
                queue.append((rr, cc))
                visited[rr][cc] = True


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_height = 0
min_height = 101
for i in range(N):
    for j in range(N):
        max_height = max(max_height, graph[i][j])
        min_height = min(min_height, graph[i][j])

ans = 0
for h in range(min_height-1, max_height+1):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and graph[r][c] > h:
                bfs(r, c, h)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
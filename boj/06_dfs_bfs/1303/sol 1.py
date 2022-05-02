import sys

def dfs(r, c):
    side = graph[r][c]
    stack = [(r, c)]
    visited[r][c] = True
    cnt = 1

    while stack:
        r, c = stack.pop()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<M and 0<=cc<N and not visited[rr][cc] and graph[rr][cc] == side:
                visited[rr][cc] = True
                stack.append((rr, cc))
                cnt += 1

    return cnt

N, M = map(int, input().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ally = 0
enemy = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == "W":
                ally += dfs(i, j)**2
            else:
                enemy += dfs(i, j)**2

print(ally, enemy)
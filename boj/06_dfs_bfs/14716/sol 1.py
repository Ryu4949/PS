M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
# visited = [[False] * N for _ in range(M)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(r, c):
    stack = [(r, c)]
    if 0<=r<M and 0<=c<N and graph[r][c] == 1:
        while stack:
            r, c = stack.pop()

            for i in range(8):
                rr, cc = r+dr[i], c+dc[i]
                if 0<=rr<M and 0<=cc<N and graph[rr][cc] == 1:
                    stack.append((rr, cc))
                    graph[rr][cc] = 0
        return True
    return False

cnt = 0
for i in range(M):
    for j in range(N):
        if dfs(i, j):
            cnt += 1

print(cnt)
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tomato = []
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            tomato.append([r, c])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for i in tomato:
        queue.append(i)

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 0:
                queue.append((rr,cc))
                graph[rr][cc] = graph[r][c] + 1

bfs()

rlt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit()
        elif graph[i][j] > rlt:
            rlt = graph[i][j]

print(rlt-1)
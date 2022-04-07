from collections import deque

M, N = map(int, input().split())
K = int(input())
graph = [[set() for _ in range(M)] for _ in range(N)]

for _ in range(K):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            graph[i-1][j-1].add(b-1)

sc, sr, gc, gr = map(int, input().split())
sc -= 1
sr -= 1
gc -= 1
gr -= 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[K+1] * M for _ in range(N)]

def bfs(r, c):
    queue = deque()
    queue.append((r, c, graph[r][c]))
    visited[r][c] = 1

    while queue:
        r, c, b = queue.popleft()
        print(f'r, c, b: {r, c, b}')

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] and visited[r][c]+1 <= visited[rr][cc]:
                bus = graph[r][c] & graph[rr][cc]
                if bus and not bus & b:
                    queue.append((rr, cc, bus))
                    visited[rr][cc] = visited[r][c] + 1
                elif bus and bus & b:
                    queue.append((rr, cc, bus))
                    visited[rr][cc] = visited[r][c]

bfs(sr, sc)

print(visited[gr][gc])



from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0 or rr >= N or cc >= M:
                continue

            if graph[rr][cc] == 0:
                continue

            if graph[rr][cc] == 1:
                graph[rr][cc] = graph[r][c] + 1
                queue.append((rr,cc))

bfs(0, 0)
print(graph[N-1][M-1])
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 1:
                graph[rr][cc] = graph[r][c] + 1
                queue.append((rr,cc))

bfs(0, 0)

print(graph[N-1][M-1])
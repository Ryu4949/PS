#bfs를 하면서 벽을 뚫은 경우도 같이 고려
#wall = 1까지는 ok
from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque([(r, c, 0)])
    visited[r][c][0] = 1

    while queue:
        r, c, w = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M:
                if visited[rr][cc][w] == 0 and graph[rr][cc] == '0':
                    queue.append((rr, cc, w))
                    visited[rr][cc][w] = visited[r][c][w] + 1
                elif graph[rr][cc] == '1' and w == 0:
                    queue.append((rr, cc, w+1))
                    visited[rr][cc][w+1] = visited[r][c][w] + 1

    if visited[N-1][M-1][0] == visited[N-1][M-1][1] == 0:
        return -1
    elif 0 in visited[N-1][M-1]:
        return max(visited[N-1][M-1])
    else:
        return min(visited[N-1][M-1])

print(bfs(0, 0))
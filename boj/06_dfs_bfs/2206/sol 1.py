#bfs를 하면서 뚫은 벽을 카운트 해줄 변수를 같이 사용
#wall = 1까지는 ok 2가되면 No
#틀린답
from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, w):
    queue = deque([(r, c, w)])
    visited[r][c] = 1

    while queue:
        r, c, w = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and visited[rr][cc] == 0:
                if graph[rr][cc] == '0':
                    queue.append((rr, cc, w))
                    visited[rr][cc] = visited[r][c] + 1
                elif graph[rr][cc] == '1' and w < 1:
                    queue.append((rr, cc, w+1))
                    visited[rr][cc] = visited[r][c] + 1

    if not visited[N-1][M-1]:
        return -1
    else:
        return visited[N-1][M-1]

print(bfs(0, 0, 0))
from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
rules = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)

def bfs():
    visited = [[INF] * C for _ in range(R)]
    queue = deque()
    for i in range(C):
        if graph[0][i] == 1:
            queue.append((0, i))
            visited[0][i] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(N):
            rr, cc = r+rules[i][0], c+rules[i][1]

            if 0<=rr<R and 0<=cc<C and visited[rr][cc] == INF and graph[rr][cc] == 1:
                if rr == R-1:
                    return visited[r][c] + 1
                visited[rr][cc] = visited[r][c] + 1
                queue.append((rr, cc))

    return INF

ans = bfs()

if ans == INF:
    print(-1)
else:
    print(ans)